import random

import factory

from django.contrib.gis.geos.point import Point

from car.models import Car
from car.factories.user import UserFactory
from car import constants
from car.factories.carmodel import CarModelFactory


class CarFactory(factory.django.DjangoModelFactory):
    current_location = factory.Sequence(lambda n: Point(random.uniform(52.0, 53.0), random.uniform(13.0, 14.0)))
    user = factory.RelatedFactory(UserFactory)
    current_status = factory.Sequence(lambda n: random.choice(constants.STATUSES)[0])
    model = factory.RelatedFactory(CarModelFactory)

    class Meta:
        model = Car