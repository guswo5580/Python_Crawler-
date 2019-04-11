import urllib.request
import bs4
url = "https://www.naver.com"
html = urllib.request.urlopen(url)
# url 을 연결하여 오픈

bsObj = bs4.BeautifulSoup(html, "html.parser")
# bs4를 통해 정보를 pasing

# print(html.read())
# 정돈되지 않고 정보 그대로 추출
# print(bsObj)

#원하는 부분을 추출하는 과정
info = bsObj.find("div", {"class" : "area_links"})
# 감싸고 있는 태그 -> class -> 네임
print(info)

moreinfo = info.find('a')
print(moreinfo.text)