from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse

pageString = crawl('')
products = parse(pageString)
print(products)