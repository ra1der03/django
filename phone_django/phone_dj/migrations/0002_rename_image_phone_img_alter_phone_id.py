# Generated by Django 5.0.3 on 2024-03-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_dj', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='image',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
