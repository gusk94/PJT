from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre, Review
from .serializers import MovieSerializer, GenreSerializer, GenreDetailSerializer, ReviewSerializer


@api_view(['GET'])
def genre_list(request):
    params = {}
    genre_pk = request.GET.get('genre_pk')
    if genre_pk is not None:
        params['genre_pk'] = genre_pk
    genres = Genre.objects.filter(**params)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_movie(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    params = {}
    movie_pk = request.GET.get('movie_pk')
    if movie_pk is not None:
        params['movie_pk'] = movie_pk
    movies = Movie.objects.filter(**params)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_reviews(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk, user_id=1)
    return Response({'message': '작성되었습니다.'})


# PUT : 전부 다 수정 / FETCH : 원하는 부분만 수정
@api_view(['GET', 'PUT', 'DELETE'])
def update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})
