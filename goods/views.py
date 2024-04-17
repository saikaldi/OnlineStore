from django.shortcuts import render
from goods.models import Products, Categories
# Create your views here.

def catalog(request):
    context = {
        'title': 'Welcome Home',
        'goods': [
            {'image': 'deps/images/goods/dress1.jpg',
             'name': 'T-Shirt',
             'description': 'A white T-shirt is a classic wardrobe essential, offering comfort and versatility.',
             'price': 150.00},

            {'image': 'deps/images/goods/ipad-case2.jpg',
             'name': 'Ipad Case',
             'description': 'Introducing the sleek and functional iPad case, designed to provide both style and protection for your device.',
             'price': 93.00},

            {'image': 'deps/images/goods/bag-1.jpg',
             'name': 'Girls super bag',
             'description': 'The stylish and versatile bag designed to meet all your needs.',
             'price': 670.00},

            {'image': 'deps/images/goods/bag-3.jpg',
             'name': 'Blush Blossom" Pink Bag',
             'description': 'Elevate your style with our chic pink bag, a sophisticated accessory that adds a touch of glamour to any outfit.',
             'price': 365.00},

            {'image': 'deps/images/goods/shoes-1.jpg',
             'name': 'Shoes',
             'description': 'White Shoes for Girls: Crafted with care from pristine white materials, these shoes are pure elegance.',
             'price': 430.00},

            {'image': 'deps/images/goods/bag-2.jpg',
             'name': 'White bag',
             'description': 'This chic accessory embodies sophistication and versatility.',
             'price': 610.00},

            {'image': 'deps/images/goods/shoes-2.jpg',
             'name': '"Swan Fluff" - shoes',
             'description': '"Swan Fluff" - adorable little shoes for girls: These delicate shoes boast an elegant design and an appealing look.',
             'price': 55.00},

            {'image': 'deps/images/goods/glass1.jpg',
             'name': '"Crystal Clear" Glasses',
             'description': 'These stylish glasses are both chic and practical.',
             'price': 190.00},

            {'image': 'deps/images/goods/dress2.jpg',
             'name': '"Pink Serenade" Dress',
             'description': 'This enchanting dress is a symphony of elegance and charm.',
             'price': 30.00},

            {'image': 'deps/images/goods/glass2.jpg',
             'name': 'Black-glass',
             'description': 'These sophisticated glasses exude timeless style and versatility.',
             'price': 10.00},

            {'image': 'deps/images/goods/dress3.jpg',
             'name': 'White-dress',
             'description': 'This stunning white dress embodies elegance and grace.',
             'price': 15.00},

            {'image': 'deps/images/goods/ipad-case1.jpg',
             'name': 'Green phone case',
             'description': 'Elevate your phones style with our vibrant green case.',
             'price': 25.00},
        ]
    }



    return render(request, "goods/catalog.html", context)

def product(request):
    products = Products.objects.all()
    context = {

        'products': products
    }
    return render(request, 'goods/product.html', context)