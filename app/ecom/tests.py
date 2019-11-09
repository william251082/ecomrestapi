from datetime import datetime

from django.test import TestCase

from .models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            owner_id=1,
            release_date=datetime.now()
        )
        Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            owner_id=1,
            release_date=datetime.now()
        )

    def test_string_representation(self):
        product = Product(name="My product name")
        self.assertEqual(str(product), product.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Product._meta.verbose_name_plural), "products")
