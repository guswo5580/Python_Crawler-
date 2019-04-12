import requests
from bs4 import BeautifulSoup
#전체적으로 python package를 통해 분할아여 이용하도록

def getPageString(url) :
    # url에 requests를 적용 -- content 뽑기
    data = requests.get(url)
    return data.content

def getProducts(string) :
    # Tag를 통해 접근, 전체 제품에 접근
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id" : "productList"})
    lis = ul.findAll("li")
    # 여러 상품에 대한 묶여있는 정보를 getProduct로 보내 하나씩 원하는 정보 찾기
    products = []
    for li in lis :
        products.append(getProduct(li))
        #products객체에 push
    return products

def getProduct(li) :
    # 제품 하나에 대한 세부 내용
    img = li.find("dt", {"class" : "image"}).find("img")
    priceWrap = li.find("div", {"class" : "price-wrap"})
    strong = priceWrap.find("strong")
    return { "name" : img['alt'], "price" : strong.text}


# URL 변화를 통해 모든 페이지를 검사
categoryProducts = []
for pageNum in range(1, 18) :
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
    # url 에서 page 번호가 변화함에 따라 format을 통해 , page 번호를 바꾸어 붙여주며 for문 작성
    pageString = getPageString(url)
    # 변화하는 url을 통해 해당 페이지의 기본 content 수집
    results = getProducts(pageString)
    # categoryProducts.append(results)
    # append를 이용하면 개별 상품에 대한 정보가 아닌 하나의 페이지에 대한 정보로 묶여서 출력
    categoryProducts = categoryProducts + results

# print(len(categoryProducts))
# 하나의 객체로 담겨있는 내용을 개별로 나타냄
for result in categoryProducts :
    print(result)

