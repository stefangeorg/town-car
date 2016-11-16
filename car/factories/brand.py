import factory

from car.models import Brand


class BrandFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Model %03d" % n)

    class Meta:
        model = Brand
