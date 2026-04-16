'''
When a program or script pretends to be a browser and retrieves
web pages, looks at those web pages, extracts information, and 
then looks at more web pages.

Search engines scrape web pages - we call this "spidering the 
web" or "web crawling".

- Beautiful Soup
'''

import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.vanguardngr.com'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))