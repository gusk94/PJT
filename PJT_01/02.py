import requests
from decouple import config
from pprint import pprint
from datetime import datetime, timedelta
import csv


with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    cds = []
    for row in reader:
        cds.append(row['영화코드'])

KEY = config('KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'

movie = {}



with open('movie.csv', 'w', newline='', encoding='utf-8') as k:
    # 저장할 필드의 이름을 미리 지정
    fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt', 'showTm', 'genre', 'directors')
    csv_writer = csv.DictWriter(k, fieldnames=fieldnames)
    csv_writer.writeheader()
    for cd in cds:
        url = f'{base_url}key={KEY}&movieCd={cd}'
        response = requests.get(url)
        data = response.json()
        datas = data['movieInfoResult']['movieInfo'] 
        # print(datas)
        a = datas.get('movieCd')
        b = datas.get('movieNm')
        c = datas.get('movieNmEn')
        d = datas.get('movieNmOg')
        e = datas.get('audits')[0].get('watchGradeNm') if datas.get('audits') != [] else None
        f = datas.get('openDt')
        g = datas.get('showTm')
        h = datas.get('genres')[0].get('genreNm') if datas.get('genres') != [] else None
        i = datas.get('directors')[0].get('peopleNm') if datas.get('directors') != [] else None


        movie = {'movieCd': a, 'movieNm': b, 'movieNmEn' : c, 'movieNmOg' : d, 'audits' : e, 'openDt': f, 'showTm': g, 'genre': h, 'directors': i}   
        
        
        csv_writer.writerow(movie)
    # for item in movie():
    #     csv_writer.writerow(item)

        

# 'movieInfoResult' > 'movieInfo > movieCd / movieNm / movieNmEn / movieNmOg  'openDt' / showTm 
# 'genres' > genreNm
# 'directors' > 'peopleNm'
# 'audits' > 'watchGradeNm'


# with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
#     # 저장할 필드의 이름을 미리 지정
#     fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm')
#     writer = csv.DictWriter(f, fieldnames=fieldnames)

#     # 필드 이름을 csv 최상단에 작성



#     # Dictionary를 순회하며 key 값에 맞는 value를 한 줄씩 작성  'movieCd', 'movieNm', 'audiAcc'
#     for info in infs:
#         writer.writerow(info)