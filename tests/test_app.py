import unittest
from hello import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_healthcheck(self):
        self.assertEqual((self.app.get('/healthcheck')).status, '200 OK')

    def test_user_route(self):
        resp = self.app.get('/user/test')
        assert 'test' in resp.data.decode('utf-8')

    def test_login_route(self):
        resp = self.app.get('/login')
        self.assertEqual(resp.status, '200 OK')
