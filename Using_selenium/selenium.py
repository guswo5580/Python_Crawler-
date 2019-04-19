from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
# chrome driver를 구동

# 크롬을 통해 네이버로 접속
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디와 비밀번호를 입력( 로딩 속도를 위해 sleep 걸어주기)
sleep(0.5)
driver.find_element_by_name('id').send_keys('아이디')
# name 속성을 통해 위치를 찾고, key값으로 '' 를 전송
sleep(0.5)
driver.find_element_by_name('pw').send_keys('비밀번호')

# 로그인 버튼을 누르기 - 셀레니움에선 xpath를 이용
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 웹 페이지의 소스코드를 parsing , Beautifulsoup을 이용
# 일반적인 Beautifulsoup 이용과 셀레니움 내부에서의 이용에 유의
driver.get('https://mail.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# 메일의 제목을 파싱
title_list = soup.find_all('strong', 'mail_title')
for title in title_list :
    print(title.text)