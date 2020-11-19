from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    bio = models.TextField(max_length=500, blank=True, verbose_name='Био', default='bio')
    avatar = models.ImageField(upload_to='photos/avatars', blank=True, verbose_name='Аватарка', default='pic')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    course = models.CharField(max_length=100, blank=True, verbose_name='Курсы')
    python_access = models.BooleanField(default=False, verbose_name='Python', blank=True)
    unity3d_access = models.BooleanField(default=False, verbose_name='Unity 3D', blank=True)
    tech_svyazi_access = models.BooleanField(default=False, verbose_name='Технологии связи', blank=True)
    completed_lessons = models.CharField(max_length=250, blank=True, verbose_name='Пройденные уроки', default=0)


    def test(self):
        return self.phone

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()