from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hub.urls')),
    path('tictactoe/', include('tictactoe.urls')),
    path('memory/', include('memory_match.urls')),
    path('rps/', include('rock_paper_scissors.urls')),
]
