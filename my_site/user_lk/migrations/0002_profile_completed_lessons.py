# Generated by Django 3.0.7 on 2020-07-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_lk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='completed_lessons',
            field=models.CharField(blank=True, max_length=250, verbose_name='Пройденные уроки'),
        ),
    ]
