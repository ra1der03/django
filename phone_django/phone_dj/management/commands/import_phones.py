import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from phone_dj.models import Phone
import os
import django
from django.template.defaultfilters import slugify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'phone_dj\\phones.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for i in ['1', '2', '3']:
                for row in csv_reader:
                    if row[0] == 'id':
                        continue
                    i = Phone(id=row[0], name=row[1], img=row[2], price=int(row[3][:-2]), release_date=row[4],
                              lte_exists=row[5], slug=slugify(row[1]))
                    i.save()
