from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product


class ProductAPITest(APITestCase):

    def setUp(self):
        Product.objects.create(
            name="Laptop",
            price=50000
        )

    def test_get_products(self):
        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Laptop')
        self.assertEqual(len(response.data), 1)