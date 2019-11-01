from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
   path('genres/', views.genre_list, name='genre_list'),
   path('genres/<int:genre_pk>/', views.genre_movie, name='genre_movie'),
   path('movies/', views.movie_list, name='movie_list'),
   path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
   path('movies/<int:movie_pk>/reviews/', views.movie_reviews, name='movie_reviews'),
   path('reviews/<int:review_pk>/', views.update_delete, name='update_delete'),
]
