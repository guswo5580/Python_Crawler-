import requests
from libs.naver_shopping.parser import parse
import json

#url 분석
#query = 검색어 , pagingIndex = 페이지 번호
def crawl(pageNo) :
    url = 'https://search.shopping.naver.com/search/all.nhn?query=텀블러&pagingIndex={}&cat_id=&frm=NVSHATC'.format(pageNo)
    data = requests.get(url)
    print(data, url)
    return data.content

totalProducts = []
# 1~10 페이지까지
for pageNo in range(1, 10+1) :
    pageString = crawl(pageNo)
    products = parse(pageString)
    totalProducts += products
    #한 페이지를 불러올 때마다 totalProducts 에 넣어준다

print(totalProducts)
print(len(totalProducts))

file = open('./tumbler.json', 'w+')
file.write(json.dumps(totalProducts))