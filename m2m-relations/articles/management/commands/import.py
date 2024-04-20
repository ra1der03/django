import json

from django.core.management.base import BaseCommand
from articles.models import Article, Tag, Scope
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('articles.json', 'r') as file:
            json_data = json.loads(file.read())
            tag_main = [Tag.objects.create(name='Культура', is_main=True),
                        Tag.objects.create(name='Здоровье', is_main=True),
                        Tag.objects.create(name='Космос', is_main=True)]
            for i in range(0, 3):
                article = Article.objects.create(title=json_data[i]['fields']['title'], text=json_data[i]['fields']['text'],
                                       published_at=json_data[i]['fields']['published_at'],
                                       image=json_data[i]['fields']['image'])
                # Tag.objects.all()[i].scopes.add(Article.objects.all()[i])
                Scope.objects.create(tag=tag_main[i], article=article)
