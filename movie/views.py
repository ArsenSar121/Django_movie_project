from django.shortcuts import render, get_object_or_404
from movie.models import Movie
from django.http import Http404
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    name = request.GET.get('name', None)
    if name:
        movies = movies.filter(first_name__icontains=name)
    return render(request, 'movies/index.html', {'movies': movies})


def detail_page(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})


def add_movie(request):
    if request.GET.get('name', None):
        try:
            data = {item: val for item, val in request.GET.items()}
            Movie.objects.create(**data)
        except Exception as e:
            print(e)
            raise Http404('Invalid Arguments')
    return render(request, 'movies/add_movie.html', {})
