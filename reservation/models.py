from django.contrib.gis.db import models

from reservation import constants


class ReservationRequest(models.Model):
    start_address = models.ForeignKey('common.Address', related_name='start_addresses')
    destination_address = models.ForeignKey('common.Address', related_name='destination_addresses')
    status = models.IntegerField(constants.JOB_STATUSES, default=constants.STATUS_WAITING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estimated_start_time = models.TimeField()
    estimated_arrival_time = models.TimeField()
    car = models.ForeignKey('car.Car', null=True)
    requester = models.ForeignKey('car.User')
