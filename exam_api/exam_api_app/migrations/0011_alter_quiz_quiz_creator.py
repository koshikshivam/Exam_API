# Generated by Django 4.0.6 on 2022-07-11 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_api_app', '0010_delete_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_api_app.teacher'),
        ),
    ]
