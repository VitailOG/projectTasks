# Generated by Django 3.1.7 on 2021-10-24 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20211025_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='text',
        ),
    ]
