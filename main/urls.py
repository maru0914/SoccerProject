from django.urls import path

from main.views import HomeView, LeagueView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('league/<str:league>', LeagueView.as_view(), name='league'),
]