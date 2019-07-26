import requests
import csv

with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    movies = {}
    for row in reader:
        movies[row['movie_code']] = row['image']

for key, value in movies.items():
    image_url = value

    response = requests.get(image_url)

    with open(f'images/{key}.jpg', 'wb') as f:
        f.write(response.content)