from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse
import json

pageString = crawl('')
products = parse(pageString)
print(products)

file = open('./products.json', 'w+')
#JSON형식의 파일을 디렉토리 폴더 안에 생성 , w+ 붙여 줄것
file.write(json.dumps(products))
#생성된 JSON파일에 products의 내용 작성