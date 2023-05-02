from django.shortcuts import render
from django.http import HttpResponse

from core.models import CartOrderProducts, Product, Category, Vendor, VendorReview, CartOrder, ProductImages, ProductReview, wishlist_model, Address


def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True).order_by("-id")

    context = {
        "products": products
    }

    return render(request, 'core\index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")
    # tags = Tag.objects.all().order_by("-id")[:6]

    context = {
        "products":products,
        # "tags":tags,
    }

    return render(request, 'core/product-lists.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }
    return render(request, 'core/category-list.html', context)
