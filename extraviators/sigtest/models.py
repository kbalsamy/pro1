from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=20)

    def __str__(self):

        return self.title


@receiver(post_save, sender=Post)
def my_handler(sender, instance, created, **kwargs):

    print('signals are working')
