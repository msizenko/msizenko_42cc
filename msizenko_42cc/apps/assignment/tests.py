from django.test import TestCase, client
from django.contrib.auth.models import User


USERNAME = 'msizenko'
EMAIL = 'msizneko@gmail.com'

class TestPageTest(TestCase):
    
    def test_page(self):
        c = client.Client()
        response = c.get('/test/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world!')
        
class PersonTest(TestCase):
    fixtures = ['initial_data.json']
    
    def create_test(self):
        # user should been created from fixtures
        self.assertIsNotNone(User.objects.get(username=USERNAME))
        user = User.objects.get(username=USERNAME)
        self.assertEqual(user.username, USERNAME)
    
        # user's profile should been created automaticaly            
        self.assertIsNotNone(user.userprofile)

        
