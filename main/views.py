from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'message': 'Hello World!'

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'text': 'lorem ipsum dolor sit lorem ipsum dolor sit lorem ipsum dolor sit'
    }
    print(context)
    return render(request, 'main/about.html', context)