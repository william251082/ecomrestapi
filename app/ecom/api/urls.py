from django.urls import path

from ecom.api.views import product_list_create_api_view, product_detail_api_view, get_post_products

urlpatterns = [
    path("products/", product_list_create_api_view, name="product_list"),
    path("products/", get_post_products, name="get_post_products"),
    path("products/<int:pk>/", product_detail_api_view, name="product_detail")
]
