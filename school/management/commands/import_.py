import json

from django.core.management.base import BaseCommand
from school.models import Student, Teacher
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fixtures\\school.json', 'r') as file:
            json_data = json.loads(file.read())
            for i in range(0, 3):
                teacher = Teacher(subject_id=i+1, name=json_data[i]['fields']['name'],
                                  subject=json_data[i]['fields']['subject']).save()
            for i in range(3, 6):
                student = Student(name=json_data[i]['fields']['name'], group=json_data[i]['fields']['group'])
                student.save()
                student.teacher.add(json_data[i]['fields']['teacher'])
