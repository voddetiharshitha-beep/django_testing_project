from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):

    def test_product_creation(self):
        product = Product.objects.create(
            name="Laptop",
            price=50000
        )

        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 50000)