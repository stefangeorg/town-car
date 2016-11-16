from django.conf.urls import url

from car.views import home

urlpatterns = [

    url(r'^$', home, name='home'),
]
