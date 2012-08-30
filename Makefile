MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=msizenko_42cc.conf.test $(MANAGE) test

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=msizenko_42cc.conf.dev $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=msizenko_42cc.conf.local $(MANAGE) syncdb

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=msizenko_42cc.conf.local $(MANAGE) migrate
