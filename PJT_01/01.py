import requests
from decouple import config
from pprint import pprint
from datetime import datetime, timedelta
import csv

KEY = config('KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?'

movie_data = {}
for week in range(5, 0 , -1):
    targetDt = datetime(2019, 7, 13) - timedelta(weeks=week)
    targetDt = targetDt.strftime('%Y%m%d')
    url = f'{base_url}key={KEY}&targetDt={targetDt}&weekGb=0'
    response = requests.get(url)
    data = response.json()

    
    
    for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
        movie_data[movie.get('movieCd')] = {'영화코드':movie.get('movieCd'), '누적관객수': movie.get('audiAcc'), '영화이름':movie.get('movieNm')}

        #  code = movie.get('movieCd')
        #  if code not in movie_data: movie_data[code] = {} 라는 식으로 사용 가능
# print(movie_data)

# data['boxOfficeResult']['movieNm'] in data:
with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정
    fieldnames = ['영화코드', '누적관객수', '영화이름']
    
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_data.values():
        csv_writer.writerow(item)



