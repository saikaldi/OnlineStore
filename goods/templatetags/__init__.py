from goods.models import Categories
from django import template

def tag_categories(request):
    return Categories.objects.fall()