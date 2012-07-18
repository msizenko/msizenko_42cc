from msizenko_42cc.settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'msizenko_42cc.conf.dev.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
)
