from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall-list"),

    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall-detail"
    ),
    path("movies/", movie_list, name="movie-list"),

    path("movies/<int:pk>/", movie_detail, name="movie-detail")
]
