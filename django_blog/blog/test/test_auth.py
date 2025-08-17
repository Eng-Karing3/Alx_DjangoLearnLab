from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthFlowTests(TestCase):
    def test_register_then_login_redirects_to_profile(self):
        # register
        resp = self.client.post(reverse('register'), {
            'username': 'alice',
            'email': 'alice@example.com',
            'password1': 'StrongPassw0rd!',
            'password2': 'StrongPassw0rd!',
        })
        self.assertRedirects(resp, reverse('profile'))

        # profile loads (logged in)
        resp2 = self.client.get(reverse('profile'))
        self.assertEqual(resp2.status_code, 200)
        self.assertContains(resp2, 'Your Profile')

    def test_profile_requires_auth(self):
        resp = self.client.get(reverse('profile'))
        self.assertRedirects(resp, f"{reverse('login')}?next={reverse('profile')}")

    def test_login_page_renders(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Login')