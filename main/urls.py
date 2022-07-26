from django.urls import path

from main.views import HomeView, LeagueView, ScheduleView, StandingView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('league/<str:league_code>', LeagueView.as_view(), name='league'),
    path('schedule/<str:key>', ScheduleView.as_view(),name='schedule'),
    path('standing/<league_code>', StandingView.as_view(),name='standing'),
]