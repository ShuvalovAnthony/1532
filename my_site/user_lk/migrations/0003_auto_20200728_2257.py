# Generated by Django 3.0.7 on 2020-07-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_lk', '0002_profile_completed_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='completed_lessons',
            field=models.CharField(blank=True, default=0, max_length=250, verbose_name='Пройденные уроки'),
        ),
    ]