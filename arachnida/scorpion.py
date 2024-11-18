#!/usr/bin/env python3

# command to run with all jpgs in data directory
# find data -name "*.jpg" | xargs ./scorpion.py

import datetime
import os
import argparse
from venv import create
from PIL import Image, ExifTags
from colorama import Fore, Style

class Scorpion:
	
	def __init__(self, files):
		self.files = files
		self.print_data()

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

def main():
	parser = argparse.ArgumentParser(description="Print image data and Exif data from given files.")
	parser.add_argument("files", nargs="+", help="Files to print data from.")
	args = parser.parse_args()
	Scorpion(args.files)
 
if __name__ == "__main__":
	main()