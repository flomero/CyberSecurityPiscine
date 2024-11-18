#!/usr/bin/env python3

# command to run with all jpgs in data directory
# find data -name "*.jpg" | xargs ./scorpion.py

import os
import argparse
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
				exif = image._getexif()
				print(f"{Fore.GREEN}File: {Style.RESET_ALL}{file}")
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