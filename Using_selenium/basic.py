import requests
from bs4 import BeautifulSoup

MEMBER_DATA = {
    'member_ID' : 'guswo',
    'member_Password' : '12345'
}
# 하나의 세션 객체를 생성해 유지할 것

with requests.Session() as s :
# 로그인 페이지로의 POST 요청 객체를 생성
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp',
                     data=MEMBER_DATA )
# 로그인이 이루어지는 순간
print(request.text)

request = s.get('http://dowellcomputer.com/member/memberUpdateForm.jsp?ID=a')
soup = BeautifulSoup(request.text, 'html.parser')
result = soup.findAll('input', {'name' : 'memberEmail'})
# 로그인 후의 개인정보 페이지에서의 원하는 위치의 태그값을 가져오기
print(result[0].get('value'))
# 위치에 해당하는 value를 가져오기
