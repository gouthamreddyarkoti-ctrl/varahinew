from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
    })

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')