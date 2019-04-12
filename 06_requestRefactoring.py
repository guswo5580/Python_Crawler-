# 네이버 -> 금융 -> 삼성전자 금융 검색
# 리펙토링 -> 함수화
import requests
from bs4 import BeautifulSoup

def get_info(url) :
    result = requests.get(url);
    info = BeautifulSoup(result.content, "html.parser")
    return info

def get_price(company_code) :
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    info_obj = get_info(url)
    no_today = info_obj.find("p", { "class " : "no_today" })
    blind = no_today.find("span ", { "class " : "blind "})
    return blind.text

price_samsung = get_price("005930")
price_SK_hynix = get_price("000660")

print(price_samsung)
print(price_SK_hynix)






