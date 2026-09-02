from django.test import TestCase
from .models import Product


class ProductDatabaseTest(TestCase):

    def test_create_product_in_test_database(self):
        product = Product.objects.create(
            name="Monitor",
            price=15000
        )

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, "Monitor")
        self.assertEqual(product.price, 15000)

    def test_database_is_clean_for_each_test(self):
        self.assertEqual(Product.objects.count(), 0)