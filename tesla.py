import json
import openpyxl
import requests
import pprint
import xl

# Client ID : wJ8lVc_2q173a_Fz6kXj
# Client Secret : zddOvmeu7V
filename='C:\\Users\\khkpo\\Downloads\\temp.xlsx'
sheetname='temp'
contents=[]
header_param={'x-naver-client-id': 'wJ8lVc_2q173a_Fz6kXj', 'x-naver-client-secret':'zddOvmeu7V'}
url='https://openapi.naver.com/v1/search/cafearticle.json?query='
url+='테슬라 업데이트'

res=requests.get(url,headers=header_param)
pprint.pprint(res.json())

for row in res.json()['items']:
    cafename=row['cafename']
    title=row['title']
    link=row['link']
    desc=row['description']
    contents.append([cafename,title,link,desc])
print(contents)

xl.write_xl(filename,sheetname,contents)


