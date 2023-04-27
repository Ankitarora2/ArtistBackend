from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ClientManager(models.Manager):
    def create_client_for_user(self, user):
        client = self.create(user=user, name=user.username)
        return client


class Client(models.Model):
    name = models.CharField(max_length=255)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ClientManager()


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance, name=instance.username)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')
    objects = models.Manager()


class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = (
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES, default=OTHER,)
    objects = models.Manager()
