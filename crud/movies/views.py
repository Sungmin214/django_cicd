from django.shortcuts import render, redirect
from .models import Movies
from django.http import HttpResponse
from .forms import MovieForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')  # 영화 목록 페이지로 리다이렉션
    else:
        form = MovieForm()

    return render(request, 'movies/create_movie.html', {'form': form})

def delete_movie(request, movie_number):
    movie = get_object_or_404(Movies, pk=movie_number)
    movie.delete()
    return redirect('movies:index')  # 삭제 후 영화 목록 페이지로 리다이렉션