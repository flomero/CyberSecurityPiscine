import os
import re
import sys
import argparse
from urllib import request
from urllib.parse import urlparse
from colorama import Fore, Style

class Spider:

	def __init__(self, url, path, recursive, depth):
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
		self.depth = depth
		print("init with", url, path, recursive, depth)

	def log(self, level, message):
		levels = {
			"info": Fore.CYAN + "[INFO]   " + Style.RESET_ALL,
			"warning": Fore.YELLOW + "[WARNING]" + Style.RESET_ALL,
			"error": 	Fore.RED + "[ERROR]  " + Style.RESET_ALL,
			"success": Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL
		}
		print(levels.get(level, "[UNKNOWN]") + " " + message)

	def is_valid_url(self, url):
		if url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
			return True
		return False
	
	def downloadImage(self, url):
		self.log("info", "Downloading image: " + url)
		response = request.urlopen(url)
		if response.getcode() != 200:
			self.log("error", "Failed to download image: " + url)
			return
		image = response.read()
		filename = urlparse(url).hostname + urlparse(url).path
		filepath = os.path.join(self.path, filename)
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		if os.path.exists(filepath):
			self.log("warning", "Image (" + url + ") already exists: " + filepath)
			return
		with open(filepath, "wb") as file:
			file.write(image)
		self.log("success", "Image downloaded: " + url)

	def crawl(self):
		if self.is_valid_url(self.url):
			self.downloadImage(self.url)
			return;
		if not self.recursive:
			self.log("warning", "Recursion disabled. Ignoring links.")
			return
		if self.depth == 0:
			self.log("warning", "Depth level reached. Ignoring links.")
			return
		self.log("info", "Crawling: " + self.url)
		response = request.urlopen(self.url)
		if response.getcode() != 200:
			self.log("error", "Failed to crawl: " + self.url)
			return
		html = response.read()
		urls = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', str(html))
		for url in urls:
			url = url[0] + "://" + url[1] + url[2]
			if self.is_valid_url(url):
				self.downloadImage(url)
			elif self.recursive and self.depth - 1 > 0:
				s = Spider(url, self.path, self.recursive, self.depth - 1)
				s.crawl()

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