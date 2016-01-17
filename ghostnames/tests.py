from django.test import TestCase, Client
class SimpleTestHomePage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 301)

        response = self.client.get('/ghostnames/')
        self.assertEqual(response.status_code, 200)

