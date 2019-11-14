from datetime import datetime
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ecom.api.serializers import ProductSerializer
from ecom.models import Product


# initialize the APIClient app
client = Client()


class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )
        Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('get_post_products'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):
    """ Test module for GET single product API """

    def setUp(self):
        self.casper = Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )
        self.muffin = Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )
        self.rambo = Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )
        self.ricky = Product.objects.create(
            name="ipad",
            description="Sedutperspiciatis",
            body="sfgfdgsfdgsfdgs",
            location="sdffggf",
            active=True,
            # owner_id=1,
            release_date=datetime.now()
        )

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': self.rambo.pk}))
        product = Product.objects.get(pk=self.rambo.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            "name": "ProductDatum",
            "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            "body": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            "location": "Amsterdam",
            "release_date": "2019-11-18",
            "active": True,
            "created_at": "2019-11-09T06:37:22.437040Z",
            "updated_at": "2019-11-10T06:32:22.540832Z"
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.casper = Product.objects.create(
            name="casper",
            description="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            location="Amsterdam",
            release_date="2019-11-18",
            active=True,
            created_at="2019-11-09T06:37:22.437040Z",
            updated_at="2019-11-10T06:32:22.540832Z"
        )
        self.muffin = Product.objects.create(
            name="muffin",
            description="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            location="Amsterdam",
            release_date="2019-11-18",
            active=True,
            created_at="2019-11-09T06:37:22.437040Z",
            updated_at="2019-11-10T06:32:22.540832Z"
        )
        self.valid_payload = {
            "name": "ProductDatum",
            "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            "body": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            "location": "Amsterdam",
            "release_date": "2019-11-18",
            "active": True,
            "created_at": "2019-11-09T06:37:22.437040Z",
            "updated_at": "2019-11-10T06:32:22.540832Z"
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.casper = Product.objects.create(
            name="casper",
            description="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            location="Amsterdam",
            release_date="2019-11-18",
            active=True,
            created_at="2019-11-09T06:37:22.437040Z",
            updated_at="2019-11-10T06:32:22.540832Z"
        )
        self.muffin = Product.objects.create(
            name="muffin",
            description="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta",
            location="Amsterdam",
            release_date="2019-11-18",
            active=True,
            created_at="2019-11-09T06:37:22.437040Z",
            updated_at="2019-11-10T06:32:22.540832Z"
        )

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)