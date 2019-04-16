import pandas as pd

df = pd.read_json('./products.json')

writer = pd.ExcelWriter('products.xlsx')
df.to_excel(writer, 'sheet1')
writer.save()


# Excel 파일로의 기본 변환
# writer = pd.ExcelWriter(filename)
# for dict in dicts :
#     dict['df'].to_exel(writer, dict['sheetName'])
# writer.save()