# Generated by Django 4.0.6 on 2022-07-11 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_api_app', '0003_examcreater_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examcreater',
            name='solution',
        ),
    ]
