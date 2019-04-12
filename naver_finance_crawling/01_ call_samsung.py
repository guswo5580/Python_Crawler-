import requests
from bs4 import BeautifulSoup

#using requests and bs4 for getting data from naver finance
def get_page(company_code) :
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    page = BeautifulSoup(result.content, "html.parser")
    return page

def get_today_price(company_code) :
    page = get_page(company_code)
    no_today = page.find("p" , { "class" : "no_today" })
    blind_now = no_today.find("span" , { "class" : "blind"})
    return blind_now.text

company_codes = ["005930", "000660", "005680"]
for item in company_codes :
    price = get_today_price(item)
    print(price)



