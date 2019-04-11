from urllib.request import urlopen
import bs4

url = "https://news.naver.com"
html = urlopen(url)

bsObj = bs4.BeautifulSoup(html.read(), "html.parser")
ul = bsObj.find("ul", {"class" : "hdline_article_list"})
lis = ul.findAll("li")

for li in lis :
    a_tag = li.find("a")
    print("오늘의 기사는 : " , a_tag.text)