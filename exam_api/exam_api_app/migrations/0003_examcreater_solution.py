# Generated by Django 4.0.6 on 2022-07-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_api_app', '0002_registration_remove_examcreater_creater_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examcreater',
            name='solution',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
