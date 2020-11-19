# Generated by Django 3.0.7 on 2020-07-05 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='bio', max_length=500, verbose_name='Био')),
                ('avatar', models.ImageField(blank=True, default='pic', upload_to='photos/avatars', verbose_name='Аватарка')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('course', models.CharField(blank=True, max_length=100, verbose_name='Курсы')),
                ('python_access', models.BooleanField(blank=True, default=False, verbose_name='Python')),
                ('unity3d_access', models.BooleanField(blank=True, default=False, verbose_name='Unity 3D')),
                ('tech_svyazi_access', models.BooleanField(blank=True, default=False, verbose_name='Технологии связи')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]