import json
# csv 형식의 파일로 저장하는 경우
file = open("./hello.csv", "w+")
file.write("hello" + "\n")
file.write("hello2" + "\n")
file.write("hello3" + "\n")

list = []
result = "검색결과를 가져오는 로직"
list = list + result

# json 파일로 저장하는 경우
file=open("./hello2.json", "+w")
file.write(json.dumps(list))