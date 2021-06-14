from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('makeMovieData/', views.make_movieData),
    path('makeDumpData/', views.make_dumpData),
    path('rating/<int:movie_rating_pk>/', views.create_rating),
    path('<int:movie_pk>/', views.movie_detail),
    path('likes/<int:movie_pk>/',views.likes)
]