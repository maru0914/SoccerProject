from django.urls import path

from main.views import HomeView, LeagueView, ScheduleView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('league/<str:league_code>', LeagueView.as_view(), name='league'),
    path('schedule/<str:key>', ScheduleView.as_view(),name='schedule'),
]