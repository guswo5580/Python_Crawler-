from bs4 import BeautifulSoup

def getProductInfo(li) :
    img = li.find('img')
    alt = img['alt']
    #태그가 아닌 속성 접근 시 []를 이용
    priceReload = li.find('span', {'class' : '_price_reload'})
    aTit = li.find('a', {'class' : 'tit'})
    href = aTit['href']
    return { 'name' : alt , 'price' : priceReload.text.replace(',', '') ,
             'link' : href }

def parse(pageString) :
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find('ul', {'class' : 'goods_list'})
    lis = ul.findAll('li', {'class' : '_itemSection'})

    products = []
    for li in lis[:1] :
        product = getProductInfo(li)
        products.append(product)
    return products