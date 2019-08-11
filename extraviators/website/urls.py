from django.urls import path
from .views import homePage_view, pageNavigation_view, testpageview

app_name = 'website'


urlpatterns = [path('', homePage_view, name='home'),
               path('pets', pageNavigation_view, name='pets'),
               path('excessbaggage', pageNavigation_view, name='baggage'),
               path('repatriations', pageNavigation_view, name='hum'),
               path('contact', pageNavigation_view, name='contact'),
               path('test', testpageview, name='testpage'),
               ]
