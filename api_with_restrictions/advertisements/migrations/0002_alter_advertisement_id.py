# Generated by Django 5.0.6 on 2024-05-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
