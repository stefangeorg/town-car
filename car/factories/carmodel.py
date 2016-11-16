import factory

from car.models import CarModel
from car.factories.brand import BrandFactory


class CarModelFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Model %03d" % n)
    brand = factory.RelatedFactory(BrandFactory)

    class Meta:
        model = CarModel
