import pandas as pd

df = pd.read_json("json파일 경로")

#groupby - data를 기준에 따라 묶기
dfSum = df.groupby("bloggername")
dfSum.count

#blogger name 을 뽑아내기
bloggernames = df['bloggername']
print(bloggernames)