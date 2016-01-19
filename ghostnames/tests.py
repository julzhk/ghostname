from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ghostnames.views import list_names
from ghostnames.models import Username, Ghost
from ghostnames.forms import available_ghosts

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
        self.assertEqual(response.status_code, 302)

    def test_home_page_can_save_a_POST_request(self):
        self.assertEqual(Username.objects.all().count(),0)
        request = HttpRequest()
        request.method = 'POST'
        firstname = 'Andy'
        lastname = 'Alpha'
        request.POST['firstname'] = firstname
        request.POST['lastname'] = lastname
        response = list_names(request)
        self.assertEqual(Username.objects.all().count(), 1)
        created_user = Username.objects.all()[0]
        self.assertEqual(created_user.firstname, firstname)
        self.assertEqual(created_user.lastname, lastname)

    def test_home_page_saved_POST_request_now_in_context(self):
        request = HttpRequest()
        request.method = 'POST'
        firstname = 'Andy'
        lastname = 'Alpha'
        request.POST['firstname'] = firstname
        request.POST['lastname'] = lastname
        list_names(request)
        response = self.client.get('/ghostnames/')
        self.assertTrue(any(i.given_name == 'Andy Alpha' for i in response.context['ghostnames']))

    def test_home_page_saved_POST_now_choose_a_ghost_name(self):
        response = self.client.post('/ghostnames/',
                                    {'firstname': 'brian',
                                     'lastname': 'beta'}
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertTrue('choose' in response['Location'])

        response = self.client.get(response['Location'])
        self.assertTrue('brian' in response.content)
        self.assertTrue('beta' in response.content)

    def test_get_available_ghost_names_when_all_are_available(self):
        ghostnames = ['Betelgeuse','Bhoot','Bloody Mary','Bogle']
        for name in ghostnames:
            Ghost.objects.create(name=name)
        next_ghosts = available_ghosts(3)
        next_ghosts_names = [n.name for n in next_ghosts]
        for name in ghostnames[:3]:
            self.assertTrue(name in next_ghosts_names)

    def test_get_available_ghost_names_when_some_are_taken(self):
        ghostnames = ['Betelgeuse','Bhoot','Bloody Mary','Bogle']
        for i, name in enumerate(ghostnames):
            taken = 'available' if i<2 else 'taken'
            g = Ghost.objects.create(name=name, taken=taken)
        next_ghosts = available_ghosts(3)
        next_ghosts_names = [n.name for n in next_ghosts]
        for name in ghostnames[:3]:
            self.assertTrue(name in next_ghosts_names)

    def test_initialize(self):
        Ghost.initialize()
        all_ghosts_count = g = Ghost.objects.count()
        self.assertTrue(all_ghosts_count == 43)
