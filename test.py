import unittest
from app import app
from currency import convert

class CurrencyConverterTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_currencies(self):
      
        response = self.app.post('/', data=dict(from_currency='USD', to_currency='XYZ', amount='100'))
        self.assertIn(b'Invalid currency selected', response.data)

    def test_conversion(self):

        from_currency = 'USD'
        to_currency = 'EUR'
        amount = 100
        exchange_rate = 0.85  
        converted_amount = amount * exchange_rate

        result = convert(amount, exchange_rate)
        self.assertEqual(result, converted_amount)

if __name__ == '__main__':
    unittest.main()
