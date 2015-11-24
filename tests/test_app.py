import unittest
from hello import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_healthcheck(self):
        self.assertEqual((self.app.get('/healthcheck')).status, '200 OK')
