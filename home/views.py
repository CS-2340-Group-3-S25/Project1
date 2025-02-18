from django.shortcuts import render
from movies.models import Movie  # Import the Movie model

# Create your views here.

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    template_data['movies'] = Movie.objects.all()[:4]  # Get the first 4 movies
    return render(request, 'home/index.html', {'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})