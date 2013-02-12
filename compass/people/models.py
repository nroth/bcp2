from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class Person(models.Model):
    """
    A model to represent a person who has been involved in Compass.
    The intent is that anyone who has ever identified as part of
    Compass will have at least a basic entry here.  The primary goals
    are networking and record keeping.
    """

    # essential info
    first_name = models.CharField(max_length = 63)
    last_name = models.CharField(max_length = 63)

    # contact info
    street = models.CharField(max_length = 255, blank = True)
    city = models.CharField(max_length = 127, blank = True)
    state = models.CharField(max_length = 127, blank = True)
    postcode = models.CharField(max_length = 63, blank = True)
    country = models.CharField(max_length = 63, blank = True)
    phone = models.CharField(max_length = 63, blank = True)
    email = models.EmailField(max_length = 254, blank = True)

    def __unicode__(self):
        return " ".join((self.first_name, self.last_name))


class CompassUser(AbstractUser):
    """
    Extend the basic user model by allowing the association of a
    person with the user model.
    """

    person = models.OneToOneField(Person, blank = True, null = True,
                                  limit_choices_to = {"compassuser__isnull": True})

    # has the user asked to be associated with a person
    has_requested_person = models.BooleanField(default = False)

    objects = UserManager()

    def __unicode__(self):
        return " ".join((self.first_name, self.last_name))
