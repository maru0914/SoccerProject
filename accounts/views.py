from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserCreationForm
    success_message = "登録が完了しました"


class LoginPageView(LoginView):
    template_name = 'accounts/login.html'
