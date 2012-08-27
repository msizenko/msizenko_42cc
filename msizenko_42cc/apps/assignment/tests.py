from django.test import TestCase, client
from django import template
from django.core import management
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from msizenko_42cc.apps.assignment.models import RequestLog, DBLog
from msizenko_42cc.apps.assignment.forms import CalendarWidget
from msizenko_42cc import settings


USERNAME = 'admin'
PASSWORD = 'admin'
EMAIL = 'msizenko@gmail.com'

class PersonTest(TestCase):

    def setUp(self):
        self.client = client.Client()

    def create_test(self):
        user = User.objects.get(username=USERNAME)
        # user's profile should been created automaticaly            
        self.assertIsNotNone(user.userprofile)

    def user_page_test(self):
        response = self.client.get(reverse('assignment-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, EMAIL)        

class MiddlewareRequestTest(TestCase):

    def setUp(self):
        self.client = client.Client()

    def stored_request_test(self):
        self.assertEqual(RequestLog.objects.all().count(), 0)
        self.client.get(reverse('assignment-index'))
        self.assertIsNotNone(RequestLog.objects.get(method='GET'))

class ContextProcessorTest(TestCase):

    def setUp(self):
        self.client = client.Client()

    def settings_test(self):
        response = self.client.get(reverse('assignment-index'))
        # check if reqest context contains settings        
        self.assertEqual(response.context['settings'], settings)

class PersonEditTest(TestCase):

    def setUp(self):
        self.client = client.Client()
        
    def person_edit_access_test(self):
        response = self.client.get(reverse("assignment-person-edit"))
        # if user not have access to edit, server redirect him to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.login(username=USERNAME, password=PASSWORD))
        response = self.client.get(reverse('assignment-person-edit'))
        self.assertEqual(response.status_code, 200)

class CalendarWidgetTest(TestCase):

    def calendar_widget_test(self):
        calendar_widget = CalendarWidget()
        self.assertEqual(calendar_widget.render('date_of_birth', '1988-10-05'),
            u'<input type="text" class="datepicker" value="1988-10-05" name="date_of_birth" />')

class AdminEditTagTest(TestCase):

    def setUp(self):
        self.user = User.objects.get(username=USERNAME)

    def edit_link_test(self):
        self.template = template.Template('{% load edit_link from assignment_edit_link %}' \
                                          '{% edit_link user "user admin" %}'
        )
        self.context = template.Context({'user': self.user})
        rendered = self.template.render(self.context)
        self.assertEqual(rendered, u'<a href="/admin/auth/user/1/">user admin</a>\n')

class PrintModelsCommandTest(TestCase):

    def printmodels_command_test(self):
        commands = management.get_commands()
        self.assertIn('printmodels', commands)

class DBLoggerTest(TestCase):

    def db_logger_test(self):
        c1 = DBLog.objects.count()
        user = User.objects.create(username='anonymous', email='anonymous@msizenko_42cc.com')
        c2 = DBLog.objects.count()
        # If user was created, new record appears in DBLog table  
        self.assertGreater(c2, c1)

        user.first_name = 'anonymous'
        user.save()
        c3 = DBLog.objects.count()
        # If user was edited, new record appears in DBLog table  
        self.assertGreater(c3, c2)

        user.delete()
        c4 = DBLog.objects.count()
        # If user was deleted, new record appears in DBLog table  
        self.assertGreater(c4, c3)

class PrioritedReqestLogTest(TestCase):

    def setUp(self):
        self.client = client.Client()

    def priority_test(self):
        response = self.client.get(reverse('assignment-index'))
        self.assertEqual(response.status_code, 200)
        log = RequestLog.objects.all()[0]
        self.assertEqual(log.priority, 0)        
