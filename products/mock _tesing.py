from django.test import TestCase
from unittest.mock import patch

from . import services


class MockingTest(TestCase):

    @patch('products.services.get_exchange_rate')
    def test_exchange_rate_with_mock(self, mock_rate):

        mock_rate.return_value = 100

        result = services.get_exchange_rate()

        self.assertEqual(result, 100)

        mock_rate.assert_called_once()