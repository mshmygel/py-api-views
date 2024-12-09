from rest_framework import serializers

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall
)


class MovieSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ["id", "title", "description", "duration"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = ["id", "name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta():
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]
