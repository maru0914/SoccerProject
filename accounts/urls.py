from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import LoginPageView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]