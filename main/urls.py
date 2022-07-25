from django.urls import path

from main.views import HomeView, ScheduleView

app_name = 'main'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('schedule/<str:key>', ScheduleView.as_view(),name='schedule'),
]