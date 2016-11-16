from django.contrib.gis.db import models

from car import constants


class User(models.Model):
    user = models.OneToOneField('auth.User')
    phone = models.CharField(max_length=25)


class UserAddress(models.Model):
    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=100)
    address = models.ForeignKey('common.Address')


class Car(models.Model):
    current_location = models.PointField()
    owner = models.ForeignKey('User')
    current_status = models.IntegerField(choices=constants.STATUSES, default=constants.STATUS_TAXI_UNAVAILABLE)
    model = models.ForeignKey('CarModel')
    max_trip_distance = models.FloatField(default=0)


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand')


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.IntegerField(choices=constants.DAYS)
    status = models.IntegerField(choices=constants.STATUSES, default=constants.STATUS_TAXI_UNAVAILABLE)
    exception_date = models.DateField(blank=True, null=True)
