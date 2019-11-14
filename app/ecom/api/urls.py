from django.urls import path

from ecom.api.views import get_post_products, get_delete_update_product


urlpatterns = [
    path("products/", get_post_products, name="get_post_products"),
    path("products/<int:pk>/", get_delete_update_product, name="get_delete_update_product")
]
