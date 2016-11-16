import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "User %03d" % n)
    last_name = factory.Sequence(lambda n: "Lname %03d" % n)
    email = factory.Sequence(lambda n: "email%03d@mail.com" % n)