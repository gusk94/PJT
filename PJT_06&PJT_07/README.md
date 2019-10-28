# PJT_07

### Accounts App: 유저의 회원가입과 로그인, 로그아웃 기능을 구현

### 1. URL.py

```python
from django.urls import path
from . import views

app_name= 'accounts'

urlpatterns = [
    # 유저 목록 ( /accounts/ ) 
    path('', views.index, name='index'),
    # 유저 상세보기 ( /accounts/{user_pk}/ ) 
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'), 
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password')
]
```

### 2-1. User 목록

```python
# views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model


@require_GET
def index(request):
    users = get_user_model().objects.all()
    context = {'users':users}
    return render(request, 'accounts/index.html', context)
```

```html
{% extends 'base.html' %}

{% block title %}
User
{% endblock title %}

{% block container %}
<h1>User</h1>
<form action="{% url 'accounts:signup' %}">
  {% csrf_token %}
  <button type="submit">Signup</button>
</form>
{% for user in users %}
  <ul>
    <li>
      <p>Username : <a href="{% url 'accounts:detail' user.pk %}">{{ user.username }}</a></p>
    </li>
  </ul>
{% endfor %}
{% endblock container %}
```

- driver: 현화, navigator: 성원, 가영



### 2-2. 유저 상세보기

```python
@require_GET
def detail(request, user_pk):
    user =  get_object_or_404(get_user_model(), pk=user_pk)
    context = {'user':user}
    return render(request, 'accounts/detail.html', context)
```

```html
{% extends 'base.html' %}

{% block title %}
User
{% endblock title %}

{% block container %}
<h1>User Information</h1>
{% if request.user == user %}
  <form action="{% url 'accounts:delete' %}" method="post">
    {% csrf_token %}
    <button type="submit">delete</button>
  </form>
{% endif %}
<hr>
  <h4>Comment</h4>
  {% for comment in user.comments.all %}
    <ul>
      <li><a href="{% url 'movies:detail' comment.movie.pk %}">{{ comment.movie.title }}</a> - {{ comment.score }}</li>
    </ul>
  {% endfor %}
  <hr>
  <h4>Like Movie</h4>
  {% for movie in user.like_movies.all %}
    <ul>
      <li><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></li>
    </ul>
  {% endfor %}
  <hr>
  {% include 'accounts/_follow.html' %}
{% endblock container %}
```

- driver: 현화, navigator: 성원, 가영



### Movies App

### 1 .URLS

```python
from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    # 영화 생성 (/movies/)
    path('create/', views.create, name='create'), 
    # 영화 상세보기 (/movies/{movie_pk})
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'), 
    # 평점 생성
    path('<int:movie_pk>/reviews/', views.commentcreate, name='commentcreate'), 
    # 평점 삭제
    path('<int:movie_pk>/reviews/<int:comment_pk>/delete/', views.commentdelete, name='commentdelete'),
    # 영화 좋아요 기능 구현
    path('<int:movie_pk>/like/', views.like, name='like'),
]
```

### 2-1. 영화 상세보기

```python
@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm()
    context = {'movie':movie, 'comments':comments, 'comment_form': comment_form}
    return render(request, 'movies/detail.html', context)
```

```html
{% extends 'base.html' %}

{% block title %}
Movie Info
{% endblock title %}

{% block container %}
<h1>Movie Information</h1>
User : <a href="{% url 'accounts:detail' movie.user.pk %}">{{ movie.user.username }}</a>
<br>
<hr>
<ul>
  <li>Title : {{ movie.title }}</li>
  <li>Title_en: {{ movie.title_en }}</li>
  <li>Score : {{ movie.score }}</li>
  <li>Audience : {{ movie.audience }}</li>
  <li>Open Date : {{ movie.open_date }}</li>
  <li>Genre : {{ movie.genre }}</li>
  <li>Watch Grade : {{ movie.watch_grade }}</li>
  <li>Poster : {{ movie.poster_url }}</li>
  <li>Description : {{movie.description }}</li>
</ul>
{% if request.user.is_authenticated %}
  <p>{{ movie.liked_users.all|length }} people like this movie</p>
  <form action="{% url 'movies:like' movie.pk %}">
    {% csrf_token %}
    {% if request.user in movie.liked_users.all %}
      <button type="submit">Unlike</button>
    {% else %}
      <button type="submit">like</button>
    {% endif %}
  </form>
  {% if request.user == movie.user %}
    <form action="{% url 'movies:update' movie.pk %}">
      {% csrf_token %}
      <button type="submit">Update</button>
    </form>
    <form action="{% url 'movies:delete' movie.pk %}" method="post">
      {% csrf_token %}
      <button type="submit">Delete</button>
    </form>
  {% endif %}
{% endif %}
{% if request.user.is_authenticated %}
  <form action="{% url 'movies:commentcreate' movie.pk %}" method="post">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endif %}
{% for comment in comments %}
  <ul>
    <li>
      <p>{{ comment.content }} - {{ comment.score }}</p>
      {% if request.user.is_authenticated %}
        {% if request.user == comment.user %}
            <form action="{% url 'movies:commentdelete' movie.pk comment.pk %}" method="post">
              {% csrf_token %}
              <button type="submit">delete</button>
          </form>
        {% endif %}
      {% endif %}
    </li>
  </ul>
{% endfor %}
{% endblock container %}
```

- driver: 현화, navigator: 성원, 가영

### 2-2. 영화 생성

```python
@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/create.html', context)
```

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}
Movie Index
{% endblock title %}

{% block container %}
<h1>Movies</h1>
<img src="{% static 'movies/movieimage.jpg' %}" alt="movie">
<form action="{% url 'movies:create' %}" method="post">
  {% csrf_token %}
  <button type="submit">Create</button>
</form>
{% for movie in movies %}
  <ul>
    <li>
      <p>Title : <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
      <p>Score : {{ movie.score }}</p>
    </li>
  </ul>
{% endfor %}
{% endblock container %}
```

- driver: 현화, navigator: 성원, 가영



### 2-3. 평점생성

```python
@require_POST
def commentcreate(request, movie_pk):
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie_id = movie_pk
            comment.user = request.user
            comment.save()
    return redirect('movies:detail', movie_pk)
```

```
detail.html에 있음
```

- driver: 현화, navigator: 성원, 가영



### 2-4. 평점 삭제

```python
@require_POST
def commentdelete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)
```

```html
detail.html에 있음
```

- driver: 현화, navigator: 성원, 가영



### 2-5. 영화 좋아요 기능 구현

```python 
@login_required
def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if user in movie.liked_users.all():
        user.like_movies.remove(movie)
    else:
        user.like_movies.add(movie)
    return redirect('movies:detail', movie_pk)
```

- driver: 현화, navigator: 성원, 가영 (오류수정: 성원)



- 소감
  - 짝들과 역할을 나누어 PJT를 진행해보면서 몰랐던 것들을 새롭게 배울 수 있었습니다. 배운 내용을 다시 진행해보면서 헷갈린 부분을 짝들과 정리해가며 확실하게 정리할 수 있었습니다.