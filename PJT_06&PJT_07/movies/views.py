from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from django.views.decorators.http import require_POST, require_GET
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)


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


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm()
    context = {'movie':movie, 'comments':comments, 'comment_form': comment_form}
    return render(request, 'movies/detail.html', context)


def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            if request.method == 'POST':
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                    form.save()
                    return redirect('movies:detail', movie_pk)
            else:
                form = MovieForm(instance=movie)
            context = {'form': form, 'movie': movie}
            return render(request, 'movies/update.html', context)
    return redirect('movies:detail', movie_pk)


@require_POST
def delete(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.user == movie.user:
            movie.delete()
            return redirect('movies:index')
    return redirect('movies:detail', movie_pk)


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


@require_POST
def commentdelete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)


@login_required
def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if user in movie.liked_users.all():
        user.like_movies.remove(movie)
    else:
        user.like_movies.add(movie)
    return redirect('movies:detail', movie_pk)

