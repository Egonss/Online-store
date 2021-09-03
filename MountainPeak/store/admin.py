from django import forms
from django.contrib import admin

from .models import Category, Product, ProductImage


admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_count')


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
