from django.test import TestCase

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class AuthFlowTests(APITestCase):
    def test_register_and_login(self):
        reg_url = reverse('register')
        data = {'username':'alice','email':'a@a.com','password':'Secret123'}
        r = self.client.post(reg_url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertIn('token', r.data)

        login_url = reverse('login')
        r2 = self.client.post(login_url, {'username':'alice','password':'Secret123'}, format='json')
        self.assertEqual(r2.status_code, status.HTTP_200_OK)
        self.assertIn('token', r2.data)

        token = r2.data['token']
        profile_url = reverse('profile')
        r3 = self.client.get(profile_url, HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(r3.status_code, status.HTTP_200_OK)
        self.assertEqual(r3.data['username'], 'alice')


# Create your tests here.
