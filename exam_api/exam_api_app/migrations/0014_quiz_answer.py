# Generated by Django 4.0.6 on 2022-07-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_api_app', '0013_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
