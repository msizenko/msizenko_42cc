from optparse import make_option

from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    help = 'Print all project models'
    
    option_list = BaseCommand.option_list + (
        make_option('-a',
                    '--auto-created',
                    action='store_true',
                    dest='auto_created',
                    default=False,
                    help='Print auto created models'),
    )

    def handle(self, *args, **options):
        for model in get_models(include_auto_created=options['auto_created']):
            msg = "(%d) %s.%s\n" % (model.objects.count(), model.__module__, model.__name__)
            self.stdout.write(msg)
            self.stderr.write("error: %s" % msg)
