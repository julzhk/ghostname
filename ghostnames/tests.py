from django.test import TestCase, Client
class SimpleTestHomePage(TestCase):

    def setUp(self):
        self.client = Client()

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
