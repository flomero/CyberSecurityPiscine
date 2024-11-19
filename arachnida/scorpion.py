#!/usr/bin/env python3

# command to run with all jpgs in data directory
# find data -name "*.jpg" | xargs ./scorpion.py

# for the flags
# find data -name "*.jpg" | xargs -I '{}' ./scorpion.py '{}' -d

import piexif
import datetime
import os
import argparse
from PIL import Image, ExifTags
from colorama import Fore, Style

class Scorpion:
	
	def __init__(self, files, changes = None, delete = False):
		self.files = files
		self.changes = {}
		self.print_data()
		if changes and not delete:
			try:
				self.validate_changes(changes)
			except Exception as err:
				print(f"{Fore.RED}Error: {err}{Style.RESET_ALL}")
				return
			self.modify_exif()
			self.print_data()
		elif delete:
			self.delete_exif()
			self.print_data()

	def validate_changes(self, changes):
		for change in changes:
			try:
				tag, value = change.split("=")
			except ValueError:
				raise ValueError(f"Invalid change: {change}")
			try:
				tag = int(tag)
			except ValueError:
				raise ValueError(f"Invalid Exif tag: {tag}")
			if tag not in ExifTags.TAGS:
				raise ValueError(f"Invalid Exif tag: {tag}")
			if not value:
				raise ValueError(f"Invalid value for tag {tag}")
			self.changes[tag] = value

	def print_data(self):
		for file in self.files:
			if not os.path.exists(file):
				print(f"{Fore.RED}File not found: {Style.RESET_ALL}{file}")
				continue
			try:
				image = Image.open(file)
				print(f"{Fore.GREEN}File: {Style.RESET_ALL}{file}")
				created = datetime.datetime.fromtimestamp(os.path.getctime(file)).strftime("%Y-%m-%d %H:%M:%S")
				print(f"{Fore.CYAN}Created: {Style.RESET_ALL}{created}")
				modified = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")
				print(f"{Fore.CYAN}Modified: {Style.RESET_ALL}{modified}")
				exif = image._getexif()
				print(f"{Fore.CYAN}Format: {Style.RESET_ALL}{image.format}")
				print(f"{Fore.CYAN}Mode: {Style.RESET_ALL}{image.mode}")
				print(f"{Fore.CYAN}Size: {Style.RESET_ALL}{image.size}")
				if exif:
					print(f"{Fore.BLUE}Exif data:{Style.RESET_ALL}")
					for tag, value in exif.items():
						print(f" - {Fore.CYAN}{ExifTags.TAGS.get(tag, tag)}{Style.RESET_ALL}: {value}")
				else:
					print(f"{Fore.YELLOW}No Exif data found.{Style.RESET_ALL}")
			except Exception as err:
				print(f"{Fore.RED}Error: {err}{Style.RESET_ALL}")
			print()

	def modify_exif(self):
		for file in self.files:
			if not os.path.exists(file):
				print(f"{Fore.RED}File not found: {Style.RESET_ALL}{file}")
				continue
			try:
				image = Image.open(file)
				try:
					exif_dict = piexif.load(image.info["exif"])
				except KeyError:
					exif_dict = {"0th": {}}
				for tag, value in self.changes.items():
					exif_dict["0th"][tag] = value
				exif_bytes = piexif.dump(exif_dict)
				image.save(file, "jpeg", exif=exif_bytes)
				print(f"{Fore.GREEN}Exif data modified: {Style.RESET_ALL}{file}")
			except Exception as err:
				print(f"{Fore.RED}Error: {err}{Style.RESET_ALL}")

	def delete_exif(self):
		for file in self.files:
			if not os.path.exists(file):
				print(f"{Fore.RED}File not found: {Style.RESET_ALL}{file}")
				continue
			try:
				image = Image.open(file)
				image.save(file)
				print(f"{Fore.GREEN}Exif data deleted: {Style.RESET_ALL}{file}")
			except Exception as err:
				print(f"{Fore.RED}Error: {err}{Style.RESET_ALL}")

def main():
	parser = argparse.ArgumentParser(description="Print image data and Exif data from given files.")
	parser.add_argument("files", nargs="+", help="Files to print data from.")
	parser.add_argument("-c", "--changes", nargs="+", help="Changes to Exif data: tag=value.")
	parser.add_argument("-d", "--delete", action="store_true", help="Delete Exif data.")
	args = parser.parse_args()
	Scorpion(args.files, args.changes, args.delete)
 
if __name__ == "__main__":
	main()