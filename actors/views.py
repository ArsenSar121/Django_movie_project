from django.shortcuts import render, get_object_or_404
from actors.models import Actors
from django.db.models import Q

# Create your views here.

def index_actors(request):
    actors = Actors.objects.all()
    name = request.GET.get('first_name', None)
    if name:
        actors = actors.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
    return render(request, 'actors/index_actors.html', {'actors': actors})

def detail_actors(request, pk):
    actor = get_object_or_404(Actors, pk = pk)
    return render(request, 'actors/detail_actors.html', {"actor": actor})
