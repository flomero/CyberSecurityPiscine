#!/usr/bin/env python3

import os
import re
import sys
import argparse
import requests
from urllib.parse import urlparse
from colorama import Fore, Style
from bs4 import BeautifulSoup as bs

URL_REGEX = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'
FILE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

TAG_ATTR_COMBS = {
	"a": ["href"],
	"applet": ["codebase", "archive"],
	"area": ["href"],
	"base": ["href"],
	"blockquote": ["cite"],
	"body": ["background"],
	"del": ["cite"],
	"form": ["action"],
	"frame": ["longdesc", "src"],
	"head": ["profile"],
	"iframe": ["longdesc", "src"],
	"img": ["longdesc", "src", "usemap", "srcset"],
	"input": ["src", "usemap", "formaction"],
	"ins": ["cite"],
	"link": ["href"],
	"object": ["classid", "codebase", "data", "usemap", "archive"],
	"q": ["cite"],
	"script": ["src"],
	"audio": ["src"],
	"button": ["formaction"],
	"command": ["icon"],
	"embed": ["src"],
	"html": ["manifest"],
	"source": ["src", "srcset"],
	"track": ["src"],
	"video": ["poster", "src"],
	"svg": ["href"],
	"image": ["href"],
	"div": ["style"],
	"span": ["style"],
	"p": ["style"],
}

class Spider:

	def __init__(self, url, path, recursive, depth = 0):
		try:
			self.url = self.validate_url(url)
			self.path = self.validate_path(path)
		except ValueError as err:
			self.log("error", str(err))
			sys.exit(1)
		self.recursive = recursive
		self.depth = depth if recursive else 0

		if recursive and depth is None:
			self.depth = 5

		self.log("info", "Spider initialized with URL: " + url)
		self.log("info", "Path: " + path)
		self.log("info", "Recursion: " + str(recursive))
		self.log("info", "Depth: " + str(depth))
  
	@staticmethod
	def validate_path(path):
		if os.path.exists(path) and not os.path.isdir(path):
			raise ValueError(f"Invalid path: {path} (not a directory)")
		os.makedirs(path, exist_ok=True)
		return path

	@staticmethod
	def validate_url(url):
		if not re.match(URL_REGEX, url):
			raise ValueError(f"Invalid URL: {url}")
		return url

	@staticmethod
	def log(level, message):
		levels = {
			"info": Fore.CYAN + "[INFO]   " + Style.RESET_ALL,
			"warning": Fore.YELLOW + "[WARNING]" + Style.RESET_ALL,
			"error": 	Fore.RED + "[ERROR]  " + Style.RESET_ALL,
			"success": Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL
		}
		print(levels.get(level, "[UNKNOWN]") + " " + message)
	
	def get_url_content(self, url):
		try:
			response = requests.get(url)
			response.raise_for_status()
		except requests.exceptions.RequestException as err:
			self.log("error", f"Request error: {err}")
			return None
		return response.content

	@staticmethod
	def match_file_type(url):
		return url.lower().endswith(tuple(FILE_EXTENSIONS))
	
	def saveImage(self, url, content):
		self.log("info", "Saving image: " + url)
		filename = urlparse(url).hostname + urlparse(url).path
		filepath = os.path.join(self.path, filename)
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		if os.path.exists(filepath):
			self.log("warning", "Image (" + url + ") already exists: " + filepath)
			return
		with open(filepath, "wb") as file:
			file.write(content)
		self.log("success", "Saved image: " + url)

	def crawl(self):
		self.log("info", "Crawling: " + self.url)
		content = self.get_url_content(self.url)
		if not content:
			return
		if self.match_file_type(self.url):
			self.saveImage(self.url, content)
		if not self.recursive or self.depth <= 0:
			return
		soup = bs(content, "html.parser")
		urls = []
		for tag, attrs in TAG_ATTR_COMBS.items():
			for attr in attrs:
				for link in soup.find_all(tag):
					if attr in link.attrs:
						if link[attr].startswith("/"):
							link[attr] = self.url.rstrip("/") + link[attr]
							urls.append(link[attr])
		try:
			regex_urls = re.findall(URL_REGEX, content.decode())
		except UnicodeDecodeError:
			regex_urls = []
		for url in regex_urls:
			url = url[0] + "://" + url[1] + url[2]
			urls.append(url)
		urls = list(set(urls))
		for url in urls:
			if self.depth - 1 > 0 or (self.depth - 1 == 0 and self.match_file_type(url)):
				s = Spider(url, self.path, self.recursive, self.depth - 1)
				s.crawl()


if __name__ == "__main__":
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