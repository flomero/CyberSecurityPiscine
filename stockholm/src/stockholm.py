import argparse
import typing
from colorama import Fore, Style
import sys

class Stockholm:
	def __init__(self, key: str, reverse: bool, silent: bool, dry_run: bool):
		self.key = key
		self.reverse = reverse
		self.silent = silent
		self.dry_run = dry_run
		if not self.validate_key(key):
			self.log("error", "Invalid key. Key must be at least 16 characters long.")
			sys.exit(1)
			
	@staticmethod
	def log(level, message):
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



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.42')
	parser.add_argument('-r', '--reverse', type=str, help='Reverse the encryption.')
	parser.add_argument('-s', '--silent', action='store_true', help='Silent mode.')
	parser.add_argument('-u', '--dry-run', action='store_true', help='Dry run (no encryption - just printing what would be done).')
	# add more help to the parser
	args = parser.parse_args()
 
if __name__ == '__main__':
	main()