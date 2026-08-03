from django.urls import path
from . import views

app_name = 'memory_match'

urlpatterns = [
    path('', views.index, name='index'),
]
