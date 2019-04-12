import requests
from bs4 import BeautifulSoup

# 기본 첫 페이지 가져오기
url = "http://www.netd.ac.za/?action=browse&category=Affiliation&order=asc"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

# 페이지 내에 있는 이동 링크 추출하기
basic_url = "http://www.netd.ac.za/"
ol = bs_obj.find("ol", {"start" : "1"})
lis = ol.findAll("li")
for li in lis :
    # print(li.find("a")["href"])
    print(basic_url + li.find("a")["href"])

# 문제점 : 1, 2, 3 ... 항목에 따라 페이지의 주소가 바뀐다
# url 에서 변화하는 규칙을 찾아내어 모듈화를 통해 크롤링
