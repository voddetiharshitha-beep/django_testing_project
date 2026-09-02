from django.test import TestCase
from .models import Product


class ProductFixtureTest(TestCase):

    fixtures = ['products/products.json']

    def test_fixture_data_loaded(self):
        products = Product.objects.all()

        self.assertEqual(products.count(), 3)

    def test_laptop_exists(self):
        laptop = Product.objects.get(name="Laptop")

        self.assertEqual(laptop.price, 50000)