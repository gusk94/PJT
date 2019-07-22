# Project 01

### 영화 데이터 불러오기 

* 영화진흥위원회 오픈 API 를 사용하여 주간TOP10 , 영화정보, 감독정보를 불러옴.
* 오픈 API에서 받은 KEY 값은 .env를 통해서 안전하게 보관해줌.

1. 주간 박스오피스 데이터

   requests와 datetime모듈을 사용

   for문과 datetime의 timedelta를 사용해 50주의 차이를 만들고 requests를 이용해 url을 불러옴

   불러온 data에서 필요한 정보만 가져와 새로운 dictionary를 만들어 csv파일에 저장

2. 영화 정보

   1번에서 만든 csv파일을 읽어와 영화코드를 새롭게 저장

   영화 정보를 가지고 있는 새로운 url을 불러와 필요한 정보만 골라 새로운 csv파일을 만듦

3. 감독 정보

   영화 정보를 저장한 csv파일에서 감독명을 골라와 새로운 url에 입력

   필요한 감독 정보를 골라와 csv파일에 저장함

* 주간 박스오피스

  ![1 boxoffice](https://user-images.githubusercontent.com/52534963/61600314-fb0db080-ac6a-11e9-8303-92f63b47dd28.PNG)

* 영화 정보

  ![2movie](https://user-images.githubusercontent.com/52534963/61600332-1678bb80-ac6b-11e9-97d1-7c44e77f5788.jpg)

* 감독 정보

  ![3 director](https://user-images.githubusercontent.com/52534963/61600354-2c867c00-ac6b-11e9-9399-29403232ac00.PNG)

