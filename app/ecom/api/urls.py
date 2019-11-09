from django.urls import path

from ecom.api.views import product_list_create_api_view, product_detail_api_view

urlpatterns = [
    path("products/", product_list_create_api_view, name="product-list"),
    path("products/<int:pk>/", product_detail_api_view, name="product-detail")
]
