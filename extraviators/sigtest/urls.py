from django.urls import path
from .views import ajaxrequest, sigtesthome

app_name = 'sigtest'


urlpatterns = [
    path('sigtest', sigtesthome, name='shome'),
    path('test', ajaxrequest, name='test'),

]
