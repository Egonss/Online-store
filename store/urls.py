from django.views.generic import DetailView
from django.urls import path
from .models import Product
from .views import category_view
app_name = "store"

urlpatterns = [
    path('category/<str:name>', category_view, name="category"),
    path('product/<int:pk>', DetailView.as_view(model=Product), name="product-detail")
]
