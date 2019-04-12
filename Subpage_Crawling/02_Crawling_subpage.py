import requests
from bs4 import BeautifulSoup

def getLinks(start) :
    url = "http://www.netd.ac.za/portal/?action=browse&category=Affiliation&maxresults=10&start=" + str(start) + "&order=asc"
    # start는 int형으로 넘어올 것 => str()으로 감싸줄 것
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    # 페이지 내에 있는 이동 링크 추출하기
    basic_url = "http://www.netd.ac.za/"
    ol = bs_obj.find("ol")
    lis = ol.findAll("li")
    links = []
    for li in lis :
        # print(li.find("a")["href"])
        link = basic_url + li.find("a")["href"]
        links.append(link)
        # list 에 요소 추가 (push)
    return links

def get_subPage(pagecount) :
    for n in range(pagecount) :
        result_links = getLinks(n*1 + 1)
        # link를 타고 넘어가 title 가져오기
        for result_link in result_links :
            # 받은 link를 토대로 새롭게 requests, beautifulsoup 적용 
            sub_link = requests.get(result_link)
            sub_obj = BeautifulSoup(sub_link.content , "html.parser")
            title = sub_obj.find("td")
            print(title.text)

print(get_subPage(3))
