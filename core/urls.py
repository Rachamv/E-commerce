from django.urls import path
from core.views import index, category_list_view, product_list_view, category_product_list__view, vendor_list_view, vendor_detail_view, product_detail_view


# add_to_cart, add_to_wishlist, ajax_add_review, ajax_contact_form, cart_view, , checkout_view, customer_dashboard, delete_item_from_cart, filter_product, index, make_address_default, order_detail, payment_completed_view, payment_failed_view, ,  remove_wishlist, search_view, tag_list, update_cart,   wishlist_view, contact, about_us, purchase_guide, privacy_policy, terms_of_service

app_name = "core"

urlpatterns = [
     # Homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),

    # Vendor
    path("vendor/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),
]