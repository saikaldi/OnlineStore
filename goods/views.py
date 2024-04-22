from django.shortcuts import render
from goods.models import Products, Categories
# Create your views here.

def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Home',
        'products': goods
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    products = Products.objects.all()
    context = {

        'products': products
    }
    return render(request, 'goods/product.html', context)