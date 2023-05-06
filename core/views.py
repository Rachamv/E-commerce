from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Avg
from core.models import CartOrderProducts, Product, Category, Vendor, VendorReview, CartOrder, ProductImages, ProductReview, wishlist_model, Address


def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(
        product_status="published", featured=True).order_by("-id")

    context = {
        "products": products
    }

    return render(request, 'core\index.html', context)

def home(request):
    return render(request, 'core\home.html')


def product_list_view(request):
    products = Product.objects.filter(
        product_status="published").order_by("-id")
    # tags = Tag.objects.all().order_by("-id")[:6]

    context = {
        "products": products,
        # "tags":tags,
    }

    return render(request, 'core/product-lists.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    # categories = Category.objects.all().annotate(product_count=("product")) /// another method for product counting

    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)


def category_product_list__view(request, cid):
    category = Category.objects.get(cid=cid) # food, Cosmetics
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category":category,
        "products":products,
    }
    return render(request, "core/category-product-list.html", context)

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors": vendors,
    }
    return render(request, "core/vendor-list.html", context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published").order_by("-id")

    context = {
        "vendor": vendor,
        "products": products,
    }
    return render(request, "core/vendor-detail.html", context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    # Getting all reviews related to a product
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting average review
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # Product Review form
    review_form = ProductReviewForm()


    make_review = True 

    if request.user.is_authenticated:
        address = Address.objects.get(status=True, user=request.user)
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False
    
    address = "Login To Continue"


    p_image = product.p_images.all()

    context = {
        "p": product,
        "address": address,
        "make_review": make_review,
        "review_form": review_form,
        "p_image": p_image,
        "average_rating": average_rating,
        "reviews": reviews,
        "products": products,
    }

    return render(request, "core/product-detail.html", context)