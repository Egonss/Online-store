from django.shortcuts import render
from django.forms import Form, BooleanField, CharField, ChoiceField, ModelChoiceField

from .models import Product, Category


def category_view(request, name):
    products = Product.objects.filter(categories__name=name)

    return render(request, "store/category.html",
                  {'products': products,
                   'category_name': name})


ORDER_CHOICES = [
    ('PRICE_ASC', 'Price (lowest first)'),
    ('PRICE_DESC', 'Price (highest first)'),
    ('NAME', 'Name')
]


class FilterForm(Form):
    name = CharField(required=False)
    categories = ModelChoiceField(
        queryset=Category.objects.all(), required=False)
    order_by = ChoiceField(choices=ORDER_CHOICES, required=False)
    only_in_stock = BooleanField(
        label="Only select products that are in stock.", required=False)


def filter_view(request):
    form = FilterForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        categories = form.cleaned_data['categories']
        order_by = form.cleaned_data['order_by']
        only_in_stock = form.cleaned_data['only_in_stock']

        products = Product.objects.filter(
            name__icontains=name).prefetch_related('images')
        if categories:
            products = products.filter(categories=categories)

        if only_in_stock:
            products = products.filter(stock_count__gt=0)

        if order_by == "NAME":
            products = products.order_by('name')
        else:
            products = products.order_by('price')
            if order_by == 'PRICE_DESC':
                products = products.reverse()

    else:
        # Incorrect form submission? Just get everything.
        products = Product.objects.all()
    return render(request, "store/filter.html", {'form': form, 'products': products})
