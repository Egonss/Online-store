from django.shortcuts import render

# Create your views here.
from .models import Product, Category


def category_view(request, name):
    products = Product.objects.filter(category__name=name)
    return render(request, "store/category.html", {'products': products, 'category_name': name})
