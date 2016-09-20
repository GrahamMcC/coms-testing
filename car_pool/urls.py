from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_cars, name='post_cars'),
    url(r'^car/(?P<pk>[0-9]+)/$', views.car_detail, name='car_detail'),
    url(r'^car/new/$', views.new_car, name='new_car'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
    url(r'^user/new/$', views.new_user, name='new_user'),
    url(r'^car/(?P<pk>\d+)/booked/$', views.car_booked, name='car_booked'),
]
