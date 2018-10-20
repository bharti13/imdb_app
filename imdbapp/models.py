from django.db import models

# class Movie(models.Model):
#     name = models.CharField(max_length=200)
#     director = models.CharField(max_length=200)
#     popularity = models.CharField(max_length=200)
#     genre = models.CharField(max_length=200)
#     imdb_score = models.CharField(max_length=200)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
    popularity = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name


class Genre(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
        # return str(int(self.id))


class MovieGenre(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return str(int(self.id))