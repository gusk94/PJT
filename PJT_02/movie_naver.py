import requests
from decouple import config
from pprint import pprint
import time
import csv

with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    movies = {}
    for row in reader:
        movies[row['영화 대표코드']] = row['영화명(국문)']


ID = config('CLIENT_ID')
SECRET = config('CLIENT_SECRET')
base_url = 'https://openapi.naver.com/v1/search/movie.json'
HEADER = {
    "X-Naver-Client-Id": ID,
    "X-Naver-Client-Secret": SECRET
}

with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as k:
    fieldnames = ('movie_code', 'link', 'image', 'Rating')
    csv_writer = csv.DictWriter(k, fieldnames=fieldnames)
    csv_writer.writeheader()
    for key, value in movies.items():
        time.sleep(0.1)
        url = f'{base_url}?query={value}'
        
        datas = requests.get(url, headers=HEADER).json()

        item = datas['items']
        
        if datas['items']:
            info = {'movie_code' : key}
            info['link'] = datas['items'][0]['link']
            info['image'] = datas['items'][0]['image']
            info['Rating'] = datas['items'][0]['userRating']

            csv_writer.writerow(info)