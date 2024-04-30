from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Home - Authentication Page'
    }
    return render(request, 'users/login.html', context)

def registration(request):
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
    pass