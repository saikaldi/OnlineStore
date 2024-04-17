from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'Welcome to home page',
        'categories': categories

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'text': 'lorem ipsum dolor sit lorem ipsum dolor sit lorem ipsum dolor sit'
    }
    print(context)
    return render(request, 'main/about.html', context)