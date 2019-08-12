from django.db import models

# Create your models here.


class ExcessBaggageEnquiry(models.Model):

    destination = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    Baggage_detail = models.TextField()
    created_on = models.DateField(auto_now=True)

    def __str__(self):

        return str(self.id)


class PetsRelocationEnquiry(models.Model):

    destination = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    saluatation = models.CharField(max_length=5)
    firstname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.IntegerField()
    Baggage_detail = models.TextField()
    created_on = models.DateField(auto_now=True)

    def __str__(self):

        return str(self.id)
