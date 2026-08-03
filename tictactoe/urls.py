from django.urls import path
from . import views

app_name = 'tictactoe'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/ai-move/', views.ai_move, name='ai_move'),
]
