#!/bin/bash/python3
import argparse
import ipaddress
import typing
import re

class Inquisitor:
	def __init__(self, ipsrc: str, macsrc: str, ipdst: str, macdst: str) -> None:
		self.ipsrc = ipsrc
		self.macsrc = macsrc
		self.ipdst = ipdst
		self.macdst = macdst
		if not self.check_ip(self.ipsrc):
			raise ValueError('Invalid IP address for source')
		if not self.check_ip(self.ipdst):
			raise ValueError('Invalid IP address for destination')
		if not self.check_mac(self.macsrc):
			raise ValueError('Invalid MAC address for source')
		if not self.check_mac(self.macdst):
			raise ValueError('Invalid MAC address for destination')

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



def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument('ipsrc', help='Source IP address', type=str, required=True)
	parser.add_argument('macsrc', help='Source MAC address', type=str, required=True)
	parser.add_argument('ipdst', help='Destination IP address', type=str, required=True)
	parser.add_argument('macdst', help='Destination MAC address', type=str, required=True)
	args = parser.parse_args()
	print(f'Hello, {args.name}!')


if __name__ == '__main__':
    main()