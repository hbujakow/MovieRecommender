from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('search/', views.search),
    path('omdb/', views.omdb_search)
]