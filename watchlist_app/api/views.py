from django.http import JsonResponse

from watchlist_app.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)


def movie(request, id):
    movie = Movie.objects.get(id=id)
    data = {'movie name': movie.name,
            'movie description': movie.description,
            'movie active': movie.active
            }
    return JsonResponse(data)
