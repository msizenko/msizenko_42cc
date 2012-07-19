from django.test import TestCase, client


class TestPageTest(TestCase):
    
    def test_page(self):
        c = client.Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world!')

