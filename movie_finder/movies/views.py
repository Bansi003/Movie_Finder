# movies/views.py
from django.shortcuts import render
import requests

API_KEY = 'b8d2d49b'  # Replace with your own if needed

def home(request):
    query = request.GET.get('query')
    movies = []
    if query:
        url = f'http://www.omdbapi.com/?s={query}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print("API Response:", data)  # Debug purpose
        if data.get('Search'):
            movies = data['Search']
    return render(request, 'movies/home.html', {'movies': movies, 'query': query})

def movie_detail(request, imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)  # Debugging the API response
        if data.get('Response') == 'True':
            imdb_url = f"https://www.imdb.com/title/{data['imdbID']}/"
            data['imdb_url'] = imdb_url
            return render(request, 'movies/detail.html', {'movie': data})
        else:
            return render(request, 'movies/detail.html', {'error': 'Movie not found'})
    else:
        return render(request, 'movies/detail.html', {'error': 'Error fetching movie data'})
