# README

1. `api/v1/genres/`

   ```python
   @api_view(['GET'])
   def genre_list(request):
       params = {}
       genre_pk = request.GET.get('genre_pk')
       if genre_pk is not None:
           params['genre_pk'] = genre_pk
       genres = Genre.objects.filter(**params)
       serializer = GenreSerializer(genres, many=True)
       return Response(serializer.data)
   ```

   ![image](https://user-images.githubusercontent.com/52534963/68003449-c4efbc00-fcb0-11e9-865c-d11e8ff80237.png)

2. `api/v1/genres/{genre_pk}/`

   ```python
   @api_view(['GET'])
   def genre_movie(request, genre_pk):
       genre = get_object_or_404(Genre, pk=genre_pk)
       serializer = GenreDetailSerializer(genre)
       return Response(serializer.data)
   ```

   ![image](https://user-images.githubusercontent.com/52534963/68003478-ebadf280-fcb0-11e9-9929-c77750b37b90.png)

3. `api/v1/movies/`

   ```python
   @api_view(['GET'])
   def movie_list(request):
       params = {}
       movie_pk = request.GET.get('movie_pk')
       if movie_pk is not None:
           params['movie_pk'] = movie_pk
       movies = Movie.objects.filter(**params)
       serializer = MovieSerializer(movies, many=True)
       return Response(serializer.data)
   ```

   ![image](https://user-images.githubusercontent.com/52534963/68003544-329be800-fcb1-11e9-83c0-b7545bfd3a06.png)

4. `api/v1/movies/{movie_pk}/`

   ```python
   @api_view(['GET'])
   def movie_detail(request, movie_pk):
       movie = get_object_or_404(Movie, pk=movie_pk)
       serializer = MovieSerializer(movie)
       return Response(serializer.data)
   ```

   ![image](https://user-images.githubusercontent.com/52534963/68003604-68d96780-fcb1-11e9-87aa-16ecbdac827d.png)

5. `api/v1/movies/{movie_pk}/reiews/`

   ```python
   @api_view(['POST'])
   def movie_reviews(request, movie_pk):
       serializer = ReviewSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save(movie_id=movie_pk, user_id=request.user.pk)
       return Response({'message': '작성되었습니다.'})
   ```

   ![image](https://user-images.githubusercontent.com/52534963/68003770-2f552c00-fcb2-11e9-987f-46e6c3657ac7.png)

   ![image](https://user-images.githubusercontent.com/52534963/68003788-4431bf80-fcb2-11e9-8e41-e8a9414af4ab.png)

6. `api/v1/reviews/{review_pk}/`

   ```python
   @api_view(['GET', 'PUT', 'DELETE'])
   def update_delete(request, review_pk):
       review = get_object_or_404(Review, pk=review_pk)
       if request.method == 'GET':
           serializer = ReviewSerializer(review)
           return Response(serializer.data)
       if request.method == 'PUT':
           serializer = ReviewSerializer(data=request.data, instance=review)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response({'message': '수정되었습니다.'})
       else:
           review.delete()
           return Response({'message': '삭제되었습니다.'})
   ```

   ![image-20191101144755984](../../../AppData/Roaming/Typora/typora-user-images/image-20191101144755984.png)

   ![image](https://user-images.githubusercontent.com/52534963/68004760-1484b680-fcb6-11e9-8db3-a5b109c378f1.png)

   ![image](https://user-images.githubusercontent.com/52534963/68004365-9a076700-fcb4-11e9-840f-b744120882a8.png)

   ![image-20191101144457604](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101144457604.png)

7. `404 error`

   ![image](https://user-images.githubusercontent.com/52534963/68003911-c9b56f80-fcb2-11e9-93bf-caf6660c351a.png)

