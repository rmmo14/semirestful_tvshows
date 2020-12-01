from django.shortcuts import render, redirect
from .models import tvShow

# Create your views here.
def redir(request):
    return redirect('/shows')
    
def index(request):
    return render(request, "index.html")

def create(request):
    tvShow.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    
    return redirect('/shows')

def allshows(request):
    context = {
        'tv_shows': tvShow.objects.all()
    }
    return render(request, "allshows.html", context)

def displayshow(request, current_id):
    this_show = tvShow.objects.get(id=current_id)
    context = {
        'shows': this_show
    }
    return render(request, "showshow.html", context)

def edit(request, current_id):
    this_show = tvShow.objects.get(id=current_id)
    context = {
        'shows' : this_show
    }
    return render(request, "edit.html", context)

def update(request, current_id):
    this_show = tvShow.objects.get(id=current_id)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.release_date = request.POST['release_date']
    this_show.description = request.POST['description']
    this_show.save()
    return redirect('/shows')

def delete (request, current_id):
    this_show = tvShow.objects.get(id=current_id)
    this_show.delete()
    return redirect('/shows')