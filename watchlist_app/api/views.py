from rest_framework.response import Response
from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from watchlist_app.models import Movie


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    data = {'movie name': movie.name,
            'movie description': movie.description,
            'movie active': movie.active
            }
    return JsonResponse(data)
