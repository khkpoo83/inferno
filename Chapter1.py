import requests
from bs4 import BeautifulSoup
#https://exem.tistory.com/category/%EC%97%91%EC%85%88%20%EA%B2%BD%EC%9F%81%EB%A0%A5/DB%20%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C

res=requests.get('https://exem.tistory.com/category/%EC%97%91%EC%85%88%20%EA%B2%BD%EC%9F%81%EB%A0%A5/DB%20%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C')
soup=BeautifulSoup(res.content,'html.parser')
# content = soup.select('.course')

rows = soup.select('ul.category_list a')
for row in rows:
    print(row.string)
# for text in rows:
#     cols = text.select('td')
#     for col in cols:
#         print(col.string)
#         rst


#hobby_course_list > li:nth-child(2) > a