from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from imdbapp.serializers import MovieGenreSerializer, MovieSerializer
from .models import Movie, MovieGenre, Genre
import operator


def index(request):
    movie = Movie.objects.all().order_by('name')
    return render(request, 'imdbapp/index.html', {
        'movies': movie})


def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        movie_genre = MovieGenre.objects.filter(movie_id=movie.id).values('genre_id')
        genre_list = []
        for genre in movie_genre:
            genre_type = Genre.objects.filter(id=genre['genre_id']).values('type')
            genre_list.append(genre_type[0]['type'])
    except Movie.DoesNotExist:
        raise Http404('Movie Does Not Exist')
    return render(request, 'imdbapp/movie_detail.html',{
        'movie' : movie,
        'genre_list' : genre_list
    })


class MovieGenreViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):

        self.serializer_class = MovieSerializer
        if request.method == 'POST':
            serializer = MovieSerializer(data=request.data, many=True)
            if serializer.is_valid():
                record = serializer.save()

                movie_list = []
                for movie in record:
                    movie_list.append(movie.id)

                for index,data in enumerate(request.data):
                    for type in data["genre"]:
                        try:
                            genre_data = Genre.objects.filter(type=type).values('id')[0]
                        except:
                            Genre.objects.create(type=type)
                            genre_data = Genre.objects.filter(type=type).values('id')[0]
                        MovieGenre.objects.create(movie_id=movie_list[index], genre_id=genre_data['id'])

                return HttpResponse('success')
            else:
                return HttpResponse('failure')

        return HttpResponse('success')