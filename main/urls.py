from django.urls import path

from main.views import HomeView, LeagueView, TeamView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('league/<str:league_code>', LeagueView.as_view(), name='league'),
    path('team/<str:league_code>/<int:id>', TeamView.as_view(), name='team'),
]