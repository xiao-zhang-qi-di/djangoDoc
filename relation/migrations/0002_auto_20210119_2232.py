# Generated by Django 3.1.4 on 2021-01-19 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='invite_person',
            new_name='invite_reason',
        ),
    ]
