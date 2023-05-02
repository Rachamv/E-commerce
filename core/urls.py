from django.urls import path
from core.views import category_list_view, product_list_view, index 


# add_to_cart, add_to_wishlist, ajax_add_review, ajax_contact_form, cart_view, category_product_list__view, checkout_view, customer_dashboard, delete_item_from_cart, filter_product, index, make_address_default, order_detail, payment_completed_view, payment_failed_view, product_detail_view,  remove_wishlist, search_view, tag_list, update_cart, vendor_detail_view, vendor_list_view, wishlist_view, contact, about_us, purchase_guide, privacy_policy, terms_of_service

app_name = "core"

urlpatterns = [
     # Homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    # path("product/<pid>/", product_detail_view, name="product-detail"),

    # Category
    path("category/", category_list_view, name="category-list"),
    # path("category/<cid>/", category_product_list__view, name="category-product-list"),
]