from django.test import TestCase, client


USERNAME = 'msizenko'
EMAIL = 'msizenko@gmail.com'

class TestPageTest(TestCase):
    
    def test_page(self):
        c = client.Client()
        response = c.get('/test/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world!')
        
class PersonTest(TestCase):
    
    def setUp(self):
        self.client = client.Client()
    
    def create_test(self):
        from django.contrib.auth.models import User
        # user should been created from fixtures
        self.assertIsNotNone(User.objects.get(username=USERNAME))
        user = User.objects.get(username=USERNAME)
        self.assertEqual(user.username, USERNAME)
    
        # user's profile should been created automaticaly            
        self.assertIsNotNone(user.userprofile)
        
    def user_page_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, USERNAME)
        self.assertContains(response, EMAIL)        
        
class MiddlewareRequestTest(TestCase):
    
    def setUp(self):
        self.client = client.Client()
        
    def stored_request_test(self):
        from msizenko_42cc.apps.assignment.models import RequestLog
        self.assertEqual(RequestLog.objects.all().count(), 0)
        self.client.get('/')
        self.assertIsNotNone(RequestLog.objects.get(method='GET'))

    
        
