# Project 2

### 영화 썸네일 이미지 불러오기

1. 영화 이미지 url 및 평점

   네이버 검색 오픈 API(https://openapi.naver.com/v1/search/movie.json)를 받고 KEY와 SECRET을 발급받아서 영화 정보를 검색할 수 있는 url을 받아온다. 이 때, KEY와 SECRET은 .env를 사용해 안전하게 보관한다.

   PJT 01에서 만들었던 movie.csv에서 영화코드와 이름을 받아와 영화 url과 평점이 담긴 새로운 csv파일을 만든다.

2. 썸네일 이미지 다운

   이미지 url이 담긴 movie_naver.scv파일에서 영화코드와 이미지 url을 가져온 후, 썸네일 이미지를 'wb'타입으로 다운받는다.

* movie_naver.csv

![1 movie_naver](https://user-images.githubusercontent.com/52534963/61929242-d80a3600-afb5-11e9-9920-6ecb18d484a5.PNG)

* image파일

![2  image](https://user-images.githubusercontent.com/52534963/61929305-f708c800-afb5-11e9-9416-b7a63057144d.PNG)