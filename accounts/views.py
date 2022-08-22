from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "ログインしました。")
            return redirect('/main/home')
        else:
            messages.success(request, "ログインに失敗しました。再度試してください。")
            return redirect('/accounts/login_user')
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "ログアウトしました。")
    return redirect('/main/home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("アカウント登録が完了しました"))
            return redirect('/main/home')
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/register_user.html', {'form': form})
