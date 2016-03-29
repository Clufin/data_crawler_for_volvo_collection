import request
from import XlsxWriter
from bs4 import beautifulSoup

def bmw_collection_web_crawler(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://bmw.tmall.com/category-982546590.htm?spm=a1z10.1-b.w8731859-8876133493.7.H94ocD&search=y&catName=BMW+Lifestyle&pageNo=' + str(page)
		source_code = request.get(url)
		plain_text = source_code.text
		soup = BeuautifulSoup(plain_text)
		for link in soup.findall('a',{'class': 'item-name'})