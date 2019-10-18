# Django 를 이용해서 영화 데이터 관리하기



-  `django model` 과 `django form` 을 사용해서 데이터의 관리페이지 생성

  

### 1. 영화 데이터 모델 만들기

- Movie

  ![image](https://user-images.githubusercontent.com/52534963/67070479-1715e500-f1bb-11e9-92f4-4077c4e7355d.png)

- Comment

  ![image](https://user-images.githubusercontent.com/52534963/67070519-33198680-f1bb-11e9-8892-37fb98835eb9.png)



### 2. 영화 데이터 목록

​	![image](https://user-images.githubusercontent.com/52534963/67070401-ed5cbe00-f1ba-11e9-9bb4-bb3f7ae99881.png)



### 3. 영화 상세 데이터 보여주기

![image](https://user-images.githubusercontent.com/52534963/67070454-05ccd880-f1bb-11e9-9468-d3cc02177c0c.png)



### 4. 영화 데이터 생성, 수정 및 삭제

- **생성**

![image](https://user-images.githubusercontent.com/52534963/67070550-46c4ed00-f1bb-11e9-97b0-deb34e5acd0e.png)

- **수정**

![image](https://user-images.githubusercontent.com/52534963/67070574-593f2680-f1bb-11e9-93fa-69d461af0e5b.png)

- **삭제**

  ```python
  @require_POST
  def delete(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      movie.delete()
      return redirect('movies:index')
  ```

  



### 5. 영화 한줄평 생성 및 삭제

- **생성**

  ![image](https://user-images.githubusercontent.com/52534963/67070592-69ef9c80-f1bb-11e9-9629-2ad73355754b.png)

- **삭제**

  ```python
  @require_POST
  def commentdelete(request, movie_pk, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      comment.delete()
      return redirect('movies:detail', movie_pk)
  ```

  