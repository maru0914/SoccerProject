from django.urls import path

from main.views import HomeView, LeagueScheduleView, TeamView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('league_schedule/<str:league_code>', LeagueScheduleView.as_view(), name='league_schedule'),
    path('team/<str:league_code>/<int:id>', TeamView.as_view(), name='team'),
]