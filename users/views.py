from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from users.form import UserLoginForm, UserRegisterForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Home - Authentication Page',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'registration page'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'profile page'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))