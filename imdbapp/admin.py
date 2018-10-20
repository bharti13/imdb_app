from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, MovieGenre


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'popularity', 'imdb_score','combined_field')
    search_fields = ('name',)
    list_filter = ('director','popularity', 'imdb_score')
    ordering = ('-imdb_score',)

    def combined_field(self, obj):
        movie_name = Movie.objects.filter(name=obj.name).values('id')
        movie_id = movie_name[0]['id']
        genres = MovieGenre.objects.filter(movie_id=movie_id).values('genre_id')
        genre_list=[]
        for genre in genres:
            type = Genre.objects.get(id=genre['genre_id'])
            genre_list.append(type)
        print(genre_list)
        return genre_list

    combined_field.admin_order_field = 'genre__name'
    combined_field.short_description = 'Genre'

class GenreAdmin(admin.ModelAdmin):
	list_display = ('type',)

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('movie','genre')
    search_fields = ('movie__name', 'genre__type')
    # raw_id_fields = ('movie', 'genre')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MovieGenre, MovieGenreAdmin)