from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('minha_consulta', views.review_query, name='minha_consulta')
]
