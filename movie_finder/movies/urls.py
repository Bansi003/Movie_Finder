# movies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('movie/<str:imdb_id>/', views.movie_detail, name='movie_detail'),
]
