"""Url dispatcher for mypage app.
"""
from django.urls import path

from mypage.views import DashboardView

app_name = 'mypage'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
