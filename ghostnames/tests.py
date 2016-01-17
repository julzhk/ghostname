from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from ghostnames.views import list_names


class SimpleTestHomePage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_root_url_resolves_to_home_page_view(self):
            found = resolve('/ghostnames/')
            self.assertEqual(found.func, list_names)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = list_names(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Ghost Name Picker</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/ghostnames/')
        self.assertEqual(response.status_code, 200)

    def test_submit_name_to_create_ghost_name(self):
        """
        requirment:
        Includes a button for new users to enter their name and select a ghost name.
        """
        response = self.client.post('/ghostnames/', {'firstname': 'john',
                                                     'lastname': 'smith'}
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['ghostnames']),3)
