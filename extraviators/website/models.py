from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# from .managers import EventManager
# Create your models here.


class ExcessBaggageEnquiry(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(null=True, blank=True)
    destination_country = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    origin_country = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    baggage_detail = models.TextField()
    enquired_on = models.DateField(auto_now=True)

    def __str__(self):

        return "BAG/INQ /" + str(self.id)


class PetRelocationEnquiry(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True)
    destination_country = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    origin_country = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    pet_detail = models.TextField()
    req_depature_date = models.DateField()
    enquired_on = models.DateField(auto_now=True)

    def __str__(self):

        return "PET/INQ /" + str(self.id)


class RepatirationsEnquiry(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True)
    relationship = models.CharField(max_length=100)
    deceased_name = models.CharField(max_length=100)
    deceased_location = models.TextField()
    deceased_repatriated_to = models.TextField()
    repatriation_insurance = models.BooleanField(default=False)
    enquired_on = models.DateField(auto_now=True)

    def __str__(self):

        return "HUM/INQ /" + str(self.id)


@receiver(post_save, sender=ExcessBaggageEnquiry)
def my_handler(sender, instance, created, **kwargs):

    send_mail(
        'Subject {}'.format(instance.id),
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
