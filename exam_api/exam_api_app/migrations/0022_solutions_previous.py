# Generated by Django 4.0.6 on 2022-10-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_api_app', '0021_submit_your_answers_here_submitted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='previous',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]