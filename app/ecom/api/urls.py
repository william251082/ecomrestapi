from django.urls import path

from ecom.api.views import product_list_create_api_view, product_detail_api_view, get_post_products, get_delete_update_product


urlpatterns = [
    path("products/", product_list_create_api_view, name="product_list"),
    path("products/", get_post_products, name="get_post_products"),
    path("products/<int:pk>/", product_detail_api_view, name="product_detail"),
    path("products/<int:pk>/", get_delete_update_product, name="get_delete_update_product")
]
