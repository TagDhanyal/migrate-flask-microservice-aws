import unittest
from app import app

class IntegerArithmeticTestCase(unittest.TestCase):
    def test_base_route(self):
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Hello World!'

if __name__ == '__main__':
    unittest.main()