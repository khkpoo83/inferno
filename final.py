import requests
import xl
import re
from bs4 import BeautifulSoup

url='https://davelee-fun.github.io/trial/board/news'
prefix='https://davelee-fun.github.io/trial/board/'

res=requests.get(url)
sp=BeautifulSoup(res.content,'html.parser')

for idx,list in enumerate(sp.select('div.list_item.symph_row')[:5]):
    title=list.select_one('a.list_subject').get_text().strip()
    rpl_cnt=list.select_one('a.list_reply.reply_symph').get_text().strip()
    # Tag의 Attribute는 Dictionary 처럼 사용 가능
    link=prefix+list.select_one('a.list_subject')['href']

    print(idx + 1, title, rpl_cnt, link)

    # 댓글 용도의 추가 작업 출력
    sp2=BeautifulSoup(requests.get(link).content,'html.parser')
    repls=sp2.select('div.comment_content')
    for idx,repl in enumerate(repls):
        print('ㄴ',re.sub('[\t\n\r\f\v ]+',' ',repl.select_one('div.comment_view').get_text().strip()))






