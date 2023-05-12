from django.urls import path
app_name='players'
from . import views

urlpatterns = [
    path('', views.index, name='playerindex'),
    path('<player>', views.players_by_api, name='player'),
]