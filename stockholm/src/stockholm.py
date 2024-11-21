import argparse
import typing as tp
from colorama import Fore, Style
import sys
from cryptography.fernet import Fernet
import os

class Stockholm:
	def __init__(self, key: str, reverse: bool, silent: bool, dry_run: bool):
		self.key = key
		self.reverse = reverse
		self.silent = silent
		self.dry_run = dry_run
		if not self.validate_key(key):
			self.log("error", "Invalid key. Key must be at least 16 characters long.")
			sys.exit(1)
			
	def log(self, level: str, message: str):
		if self.silent:
			return
		levels = {
			"info": Fore.CYAN + "[INFO]   " + Style.RESET_ALL,
			"warning": Fore.YELLOW + "[WARNING]" + Style.RESET_ALL,
			"error": 	Fore.RED + "[ERROR]  " + Style.RESET_ALL,
			"success": Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL
		}
		print(levels.get(level, "[UNKNOWN]") + " " + message)

	@staticmethod
	def validate_key(key: str) -> bool:
		if len(key) < 16:
			return False
		return True

	@staticmethod
	def check_file_extension(file: str) -> bool:
		return file.endswith(".ft")

	@staticmethod
	def remove_file_extension(file: str) -> str:
		return file[:-3]

	def encrypt(self, file: str, cipher: Fernet) -> None:
		if self.check_file_extension(file):
			self.log("info", f"File '{file}' is excluded from encryption.")
			return
		with open(file, "rb") as f:
			data = f.read()
		encrypted_data = cipher.encrypt(data)
		if self.dry_run:
			self.log("success", f"Would encrypt '{file}'.")
			return
		with open(file) as f:
			f.write(encrypted_data)
		self.log("success", f"Encrypted '{file}'.")
		os.rename(file, file + ".ft")
  
	def decrypt(self, file: str, cipher: Fernet) -> None:
		if not self.check_file_extension(file):
			self.log("info", f"File '{file}' is excluded from decryption.")
			return
		if self.dry_run:
			self.log("success", f"Would decrypt '{file}'.")
			return
		with open(file, "rb") as f:
			data = f.read()
		decrypted_data = cipher.decrypt(data)
		with open(self, "wb") as f:
			f.write(decrypted_data)
		os.rename(file, self.remove_file_extension(file))
		self.log("success", f"Decrypted '{file}'.")

def main():
	parser = argparse.ArgumentParser(
		description='Stockholm - A simple encryption tool.',
		epilog='Stockholm is a simple encryption tool that uses a key to encrypt and decrypt files. This project is for educational purposes only. You should never use this type of program for malicious purposes.')
	parser.add_argument('key', type=str, help='The key to use for encryption.')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.42')
	parser.add_argument('-r', '--reverse', type=str, help='Reverse the encryption.')
	parser.add_argument('-s', '--silent', action='store_true', help='Silent mode.')
	parser.add_argument('-u', '--dry-run', action='store_true', help='Dry run (no encryption - just printing what would be done).')
	# add more help to the parser
	args = parser.parse_args()
 
if __name__ == '__main__':
	main()