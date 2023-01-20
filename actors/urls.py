from django.urls import path
from actors.views import index_actors, detail_actors

app_name = 'actors'
urlpatterns = [
    path('actors/', index_actors, name='index_actors'),
    path('detail_actors/<int:pk>/', detail_actors, name = 'detail_actors'),
]
