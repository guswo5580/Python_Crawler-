# naver API Token 받기
# naver developer -- application ( client ID , Secret )
# naver에서 제공하는 일반 code를 simplication

import requests
from urllib.parse import urlparse

keyword = '크롤링'
url = "https://openapi.naver.com/v1/search/blog?query" + keyword
# 검색 url + 검색하고자 하는 keyword를 쿼리로 전달
result = requests.get(urlparse(url).geturl(),
                      headers = {
                          "X-Naver-Client-Id" : "",
                          "X-Naver-Client-Secret" : ""
                      })
print(result.json())
