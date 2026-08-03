from django.urls import path
from . import views

app_name = 'rock_paper_scissors'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/play/', views.play_round, name='play_round'),
]
