
from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.movie_list),
    path('<int:id>/', views.movie)
]
