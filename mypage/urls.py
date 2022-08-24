"""Url dispatcher for mypage app.
"""
from django.urls import path

from mypage.views import DashboardView, SelectTeamView, register_team

app_name = 'mypage'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('select_team/', SelectTeamView.as_view(), name='select_team'),
    path('register_team/', register_team, name='register_team'),
]
