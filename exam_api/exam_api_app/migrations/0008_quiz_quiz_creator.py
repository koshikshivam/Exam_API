# Generated by Django 4.0.6 on 2022-07-11 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam_api_app', '0007_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
