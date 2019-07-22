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
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'

movie = {}

for di in dis:
    if di != '':
        # print(di)
        url = f'{base_url}key={KEY}&peopleNm={di}'

        response = requests.get(url)
        data = response.json()
        # print(data)
        datas = data['peopleListResult']['peopleList']
        # if datas != []:
        #     infos = datas[0]
        for info in data['peopleListResult']['peopleList']:
            movie[info.get('peopleNm')] = {'peopleCd': info.get('peopleCd'), 'peopleNm': info.get('peopleNm'), 'repRoleNm': info.get('repRoleNm'), 'filmoNames': info.get('filmoNames')}

#     # pprint(data)  / 'pelpleListResult' 'peopleList' ['filmoNames', 'peopleCd', 'peopleNm', 'repRoleNm']

with open('director.csv', 'w', newline='', encoding='utf-8') as k:
    # 저장할 필드의 이름을 미리 지정
    fieldnames = ('peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames')
    csv_writer = csv.DictWriter(k, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie.values():
        csv_writer.writerow(item)
