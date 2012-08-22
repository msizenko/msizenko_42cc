from msizenko_42cc.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = 'msizenko_42cc.conf.test.urls'

INSTALLED_APPS += (
    'django_nose',
    'django.contrib.admin',
    'django.contrib.admindocs',

)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
