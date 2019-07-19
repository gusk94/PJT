import requests
from decouple import config
from pprint import pprint
from datetime import datetime, timedelta
import csv


with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    dis = []
    for row in reader:
        dis.append(row['directors'])

KEY = config('KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml.json?'

movie = {}

for di in dis:
    print(di)
    url = f'{base_url}key={KEY}&peopleNm={di}'
    response = requests.get(url)
    data = response.json(encoding='utf-8')
    pprint(response)

# with open('movie.csv', 'w', newline='', encoding='utf-8') as k:
#     # 저장할 필드의 이름을 미리 지정
#     fieldnames = ('peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames')
#     for cd in cds:
#         url = f'{base_url}key={KEY}&movieCd={cd}'
#         response = requests.get(url)
#         data = response.json()
#         datas = data['movieInfoResult']['movieInfo'] 
#         # print(datas)
#         a = datas.get('movieCd')
#         b = datas.get('movieNm')
#         c = datas.get('movieNmEn')
#         d = datas.get('movieNmOg')
#         e = datas.get('audits')
#         f = datas.get('openDt')
#         g = datas.get('showTm')
#         h = datas.get('genres')
#         i = datas.get('directors')[0].get('peopleNm')


#         movie = {'movieCd': a, 'movieNm': b, 'movieNmEn' : c, 'movieNmOg' : d, 'audits' : e, 'openDt': f, 'showTm': g, 'genre': h, 'directors': i}   
        
#         csv_writer = csv.DictWriter(k, fieldnames=fieldnames)
#         csv_writer.writeheader()
#         csv_writer.writerow(movie)
