from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class AuthViewSetTest(APITestCase):
    fixtures = 'admins',
    BASE_URL = '/api'

    def setUp(self):
        self.client = APIClient()

    def assert_200(self, response):
        self.assertEqual(response.status_code, 200, response.status_code)
        self.assertTrue(response.json())

    def test_token(self):
        # Aquire a token.
        response = self.client.post(self.BASE_URL + '/auth/token/', {
            'username': 'dev@a.com',
            'password': 'a', })
        token = response.json()['token']
        self.assert_200(response)
        self.assertTrue(response.json()['token'])

        # Use token to fetch information about current user.
        response = self.client.get(self.BASE_URL + '/auth/me/', headers={
            'Authorization': f'Token abc', })
        self.assertEqual(response.status_code, 401, response.status_code)

        response = self.client.get(self.BASE_URL + '/auth/me/', headers={
            'Authorization': f'Token {token}', })
        self.assert_200(response)
        self.assertTrue(response.json()['email'])

    def test_session(self):
        response = self.client.post(self.BASE_URL + '/auth/session/', {
            'username': 'dev@a.com',
            'password': 'ab', })
        self.assertEqual(response.status_code, 400, response.status_code)

        response = self.client.post(self.BASE_URL + '/auth/session/', {
            'username': 'dev@a.com',
            'password': 'a', })
        self.assert_200(response)
