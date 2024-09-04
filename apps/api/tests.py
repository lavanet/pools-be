from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class ChainViewSetTest(APITestCase):
    fixtures = settings.STARTUP_INITIAL_FIXTURES
    BASE_URL = '/api'

    def setUp(self):
        self.client = APIClient()
        self.client.force_login(get_user_model().objects.get(email='dev@a.com'))

    def test_list(self):
        response = self.client.get(f'{self.BASE_URL}/chains/')
        self.assertEqual(response.status_code, 200)
