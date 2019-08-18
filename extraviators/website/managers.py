from django.db import models


# class EventManager(models.Manager):

#     def create_booking(self, fullname, email, mobile, destination_country, destination_city, origin_country, origin_city, bagagge_detail):

#         event = self.model(fullname=fullname, email=email, mobile=mobile,
#                            destination_country=destination_country, destination_city=destination_city,
#                            origin_country=origin_country, origin_city=origin_city, bagagge_detail=bagagge_detail)

#         event.save()
#         event.notify_admins()
#         return event
