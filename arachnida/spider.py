#!/usr/bin/env python3

import os
import re
import sys
import argparse
import requests
from urllib.parse import urlparse
from colorama import Fore, Style
from bs4 import BeautifulSoup as bs

class Spider:

	def __init__(self, url, path, recursive, depth = 0):
		if depth and not recursive:
			self.log("warning", "Depth level set without recursive flag. Ignoring depth level.")
		if os.path.exists(path) and not os.path.isdir(path):
			self.log("error", "Invalid path: " + path)
			sys.exit(1)
		elif not os.path.exists(path):
			os.makedirs(path)
		if not url.startswith("http") and not url.startswith("ftp") and not url.startswith("https"):
			self.log("error", "Invalid URL: " + url)
			sys.exit(1)
		self.url = url
		self.path = path
		self.recursive = recursive
		if recursive and depth is None:
			depth = 5
		self.depth = depth
		self.log("info", "Spider initialized with URL: " + url)
		self.log("info", "Path: " + path)
		self.log("info", "Recursion: " + str(recursive))
		self.log("info", "Depth: " + str(depth))

	def get_url_content(self, url):
		try:
			response = requests.get(url)
			response.raise_for_status()
		except requests.exceptions.RequestException as err:
			self.log("error", f"Request error: {err}")
			return None
		return response.content

	def log(self, level, message):
		levels = {
			"info": Fore.CYAN + "[INFO]   " + Style.RESET_ALL,
			"warning": Fore.YELLOW + "[WARNING]" + Style.RESET_ALL,
			"error": 	Fore.RED + "[ERROR]  " + Style.RESET_ALL,
			"success": Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL
		}
		print(levels.get(level, "[UNKNOWN]") + " " + message)

	def is_valid_url(self, url):
		if url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg')):
			return True
		return False
	
	def downloadImage(self, url):
		self.log("info", "Downloading image: " + url)
		image = self.get_url_content(url)
		if not image:
			return
		filename = urlparse(url).hostname + urlparse(url).path
		filepath = os.path.join(self.path, filename)
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		if os.path.exists(filepath):
			self.log("warning", "Image (" + url + ") already exists: " + filepath)
			return
		with open(filepath, "wb") as file:
			file.write(image)
		self.log("success", "Image downloaded: " + url)
		if url != self.url and self.recursive:
			self.crawl_recursive(image, True)
		if self.recursive:
			self.crawl_recursive(image, False)

	def crawl(self):
		if self.is_valid_url(self.url):
			self.log("info", "Starting URL is an image.")
			self.downloadImage(self.url)
			return;
		if not self.recursive:
			self.log("warning", "Recursion disabled. Ignoring links.")
			return
		if self.depth == 0:
			self.log("warning", "Depth level reached. Ignoring links.")
			return
		self.log("info", "Crawling: " + self.url)
		content = self.get_url_content(self.url)
		if not content:
			return
		soup = bs(content, "html.parser")
		for img in soup.findAll("img"):
			src = img.get("src")
			if src:
				src = self.url + src if src.startswith("/") else src
				if self.is_valid_url(src):
					self.downloadImage(src)
		self.crawl_recursive(content)

	def crawl_recursive(self, content, decrease_depth=False):
		d = self.depth
		if d is None or d == 0:
			print("Depth level reached. Ignoring links." + self.url)
			return
		if decrease_depth:
			d -= 1
		urls = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', str(content))
		for url in urls:
			url = url[0] + "://" + url[1] + url[2]
			if self.is_valid_url(url):
				self.downloadImage(url)
			elif self.recursive and d - 1 > 0:
				s = Spider(url, self.path, self.recursive, d - 1)
				s.crawl()
		if not urls:
			self.log("warning", "No links found.")


if __name__ == "__main__":
	# parse flags
	if len(sys.argv) < 2:
		print("Usage: python spider.py [-r] [-l <depth>] [-p <path>] <url>")
		sys.exit(1)
	parser = argparse.ArgumentParser(description="A simple web crawler to download images.")
	parser.add_argument("-r", help="Recursively download images", action="store_true")
	parser.add_argument("-l", help="Set depth level", type=int, nargs="?", const=5)
	parser.add_argument("-p", help="Set path where to download images", default="./data")
	parser.add_argument("url", help="URL to scrape")
	args = parser.parse_args()

	s = Spider(args.url, args.p, args.r, args.l)
	s.crawl()