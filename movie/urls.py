from django.urls import path
from movie.views import index, detail_page, add_movie

urlpatterns = [
    path('', index, name='index'),
    path('movie/detail/<int:pk>', detail_page, name='detail'),
    path('movie/add-movie/', add_movie, name='add_movie')
]