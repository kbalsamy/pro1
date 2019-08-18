from django.dispatch import receiver
from django.core.signals import post_save
from .models import ExcessBaggageEnquiry
from django.core.mail import send_mail


@receiver(signals.post_save, sender=ExcessBaggageEnquiry)
def bagEnq_received(sender, instance, created, **kwargs):
    print('booking created')
    send_mail(
        'Bagging booking - {}'.format(instance.id),
        'Message.',
        'from@example.com',
        ['john@example.com', 'jane@example.com'],
    )
