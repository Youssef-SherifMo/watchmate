
from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list),
    path('<int:id>/', movie_detail)
]
