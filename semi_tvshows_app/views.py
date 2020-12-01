from django.shortcuts import render, redirect
from .models import tvShow

# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    tvShow.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    
    return redirect('/shows/')