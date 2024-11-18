import urllib
from urllib import request
from urllib.parse import urlparse
import re
import os
import argparse
import sys

class Colors:
	red = "\033[91m"
	green = "\033[92m"
	yellow = "\033[93m"
	blue = "\033[94m"
	cyan = "\033[96m"
	reset = "\033[0m"

class Spider:

	def __init__(self, url, path="./data", recursive=False, depth=5):
		if depth and not recursive:
			self.log("warning", "Depth level set without recursive flag. Ignoring depth level.")
		if not os.path.exists(path):
			os.makedirs(path)
		if not os.path.isdir(path):
			self.log("error", "Path is not a directory: " + path)
			sys.exit(1)
		if not url.startswith("http") and not url.startswith("ftp") and not url.startswith("https"):
			self.log("error", "Invalid URL: " + url)
			sys.exit(1)
		self.url = url
		self.path = path
		self.recursive = recursive
		self.depth = depth

	def log(self, level, message):
		levels = {
			"info": Colors.cyan + "[INFO]   " + Colors.reset,
			"warning": Colors.yellow + "[WARNING]" + Colors.reset,
			"error": Colors.red + "[ERROR]  " + Colors.reset,
			"success": Colors.green + "[SUCCESS]" + Colors.reset
		}
		print(levels.get(level, "[UNKNOWN]") + " " + message)

	def is_valid_url(self, url):
		if url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".png") or url.endswith(".gif"):
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
		self.log("info", "Crawling: " + self.url)
		try:
			response = request.urlopen(self.url)
			html = response.read()
		except Exception as e:
			self.log("error", f"Failed to crawl {self.url}: {e.reason}")
			return
		urls = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', str(html))
		for url in urls:
			url = url[0] + "://" + url[1] + url[2]
			if self.is_valid_url(url):
				self.downloadImage(url)
			elif self.recursive and self.depth > 0:
				s = Spider(url, self.path, self.recursive, self.depth - 1)
				s.crawl()



if __name__ == "__main__":
	# parse flags
	if len(sys.argv) < 2:
		print("Usage: python spider.py [-r] [-l <depth>] [-p <path>] <url>")
		sys.exit(1)
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", help="Recursively download images", action="store_true")
	parser.add_argument("-l", help="Set depth level", type=int)
	parser.add_argument("-p", help="Set path where to download images")
	parser.add_argument("url", help="URL to scrape")
	args = parser.parse_args()

	recursive = False
	depth = 0
	path = "./data"

	if args.r:
		recursive = True
	if args.l and args.r:
		depth = args.l
	elif args.r:
		depth = 5
	if args.p:
		path = args.p
	
	s = Spider(args.url, path, recursive, depth)
	s.crawl()