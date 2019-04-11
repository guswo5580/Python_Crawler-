import bs4
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(bsObj)
print(bsObj.find("div"))
# find 속성으로 원하는 문자 찾는 기본