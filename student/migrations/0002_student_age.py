# Generated by Django 3.1.4 on 2021-01-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
