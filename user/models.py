from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'м'),
        (FEMALE, 'ж'),
    )
    user = models.OneToOneField(User, unique=True, null=True, db_index=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='о себе', blank=True, null=False)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, blank=True, max_length=2)
    langs = models.CharField(verbose_name='язык', blank=True, max_length=25, default='RU')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        if not created:
            instance.userprofile.save()