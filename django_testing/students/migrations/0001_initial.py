# Generated by Django 5.0.6 on 2024-06-10 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_name', models.TextField()),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_id', to='students.student')),
            ],
        ),
    ]
