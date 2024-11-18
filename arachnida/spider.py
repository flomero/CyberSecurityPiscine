import urllib
from urllib import request
from urllib.parse import urlparse
import re
import os

class Spider:

	def __init__(self, url, path="./data", recursive=False, depth=5):
		self.url = url
		self.path = path
		self.recursive = recursive
		self.depth = depth

	def is_valid_url(self, url):
		if url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".png") or url.endswith(".gif"):
			return True
		return False
	
	def downloadImage(self, url):
		response = request.urlopen(url)
		image = response.read()
		filename = urlparse(url).hostname + urlparse(url).path
		filepath = os.path.join(self.path, filename)
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		with open(filepath, "wb") as file:
			file.write(image)

	def crawl(self):
		response = request.urlopen(self.url)
		html = response.read()
		print("Scrapping: " + self.url)
		urls = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', str(html))
		for url in urls:
			url = url[0] + "://" + url[1] + url[2]
			if self.is_valid_url(url):
				self.downloadImage(url)
			elif self.recursive and self.depth > 0:
				s = Spider(url, self.path, self.recursive, self.depth - 1)
				s.crawl()



if __name__ == "__main__":
	s = Spider("http://www.google.com")
	s.crawl()