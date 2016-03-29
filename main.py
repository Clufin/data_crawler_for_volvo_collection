import requests
import xlsxwriter
from bs4 import BeautifulSoup

def bmw_collection_web_crawler(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://bmw.tmall.com/category-982546590.htm?spm=a1z10.1-b.w8731859-8876133493.7.H94ocD&search=y&catName=BMW+Lifestyle&pageNo=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"html.parser")
		for link in soup.find_all('img',{'alt':'src'}):
			pic_name = link.get('alt')
			print(pic_name)

def main():
	bmw_collection_web_crawler(2)


if __name__ == '__main__':
    main()
