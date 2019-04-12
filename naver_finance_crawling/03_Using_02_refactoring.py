import requests
from bs4 import BeautifulSoup

#using requests and bs4 for getting data from naver finance
def get_page(company_code) :
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    page = BeautifulSoup(result.content, "html.parser")
    return page

def get_candle_chart_data(company_code) :
    page = get_page(company_code)
    # close data
    td_first = page.find("td" , {"class" : "first"})
    blind = td_first.find("span", {"class" : "blind"})
    close = blind.text

    table = page.find("table", { "class" : "no_info"})
    trs = table.findAll("tr")
    # high data
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    high = first_tr_tds_second_td.find("span", {"class": "blind"}).text

    #open data
    second_tr = trs[1]
    second_tr_td_first = second_tr.find("td", {"class" : "first"})
    blind_open = second_tr_td_first.find("span", {"class" : "blind"})
    open = blind_open.text

    #low data
    second_tr_tds = second_tr.findAll("td")
    second_tr_sec_td = second_tr_tds[1]
    blind_low = second_tr_sec_td.find("span", {"class" : "blind"})
    low = blind_low.text

    return { "close" : close , "high" : high ,
             "open" : open, "low" : low }

company_codes = ["000660", "035420", "034220"]

for item in company_codes :
    print (get_candle_chart_data(item))




