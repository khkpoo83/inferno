import json
import openpyxl
import requests
import pprint

# Client ID : wJ8lVc_2q173a_Fz6kXj
# Client Secret : zddOvmeu7V
header_param={'x-naver-client-id': 'wJ8lVc_2q173a_Fz6kXj', 'x-naver-client-secret':'zddOvmeu7V'}
url='https://openapi.naver.com/v1/search/cafearticle.json?query='
url+='테슬라 업데이트'
res=requests.get(url,headers=header_param)
pprint.pprint(res.json())

