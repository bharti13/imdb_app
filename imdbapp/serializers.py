from rest_framework import serializers

from imdbapp.models import Genre, MovieGenre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie



class MovieGenreSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = MovieGenre
        fields = "__all__"
