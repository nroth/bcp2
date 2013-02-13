from django.db import models

class Contact(models.Model):
    """
    An abstract base class for models with contact information
    """

    # essential info
    name = models.CharField(max_length = 255)

    # contact info
    street = models.CharField(max_length = 255, blank = True)
    city = models.CharField(max_length = 127, blank = True)
    state = models.CharField(max_length = 127, blank = True)
    postcode = models.CharField(max_length = 63, blank = True)
    country = models.CharField(max_length = 63, blank = True)

    # other information
    comment = models.TextField(max_length = 2047, blank = True)

    # preferences
    allow_future_contact = models.BooleanField(default = True)

    @classmethod
    def search(cls, query):
        return cls.objects.filter(name__icontains=query)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    """
    An organized set of asks
    """
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 2047, blank = True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name


class Individual(Contact):
    """
    An individual who has donated to Compass in the past or that we
    plan to contact with the intent of soliciting funds.
    """

    email = models.EmailField(max_length = 254, blank = True)

    # interesting info
    relationship = models.CharField(max_length = 127, blank = True)
    point_person = models.CharField(max_length = 127, blank = True)


class Business(Contact):
    """
    A business that has donated to Compass in the past or that we plan
    to contact with the intent of soliciting goods or funds.
    """

    # many businesses have someone to contact
    contact_name = models.CharField(max_length = 255)
    contact_title = models.CharField(max_length = 255)
    contact_phone = models.CharField(max_length = 15)
    contact_email = models.EmailField(max_length = 254, blank = True)


class BusinessDonation(models.Model):
    """
    This record is for donations solicited from businesses in which we
    receieve goods or services.
    """

    # essential info
    contact = models.ForeignKey('Business')
    date = models.DateField()
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits = 12, decimal_places = 2)

    # what happened to the gift
    outcome = models.CharField(max_length=255, blank = True)


class IndividualDonation(models.Model):
    """
    This model is a container for the information we receive via email
    when someone donates via GiveToCal.
    """

    # essential info
    contact = models.ForeignKey('Individual')
    date = models.DateField()
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)

    # matching information
    matching_funds = models.BooleanField(default = False)
    matching_source = models.CharField(max_length = 255, blank = True)

    # donor-provided info
    publish = models.BooleanField(default = False)
    comments = models.CharField(max_length = 2047, blank = True)
    referrer = models.CharField(max_length = 255, blank = True)

    # administrative info
    confirmation_number = models.IntegerField(blank=True,null=True)
    fund_number = models.CharField(max_length = 31, null = True, blank = True)
    fund_description = models.CharField(max_length = 31, null =  True, blank = True)

    def __unicode__(self):
        return "${0:}- {1:}".format(self.amount, self.date)


class IndividualAsk(models.Model):
    """
    A request to an individual for funds
    """
    contacts = models.ManyToManyField('Individual')
    date = models.DateField()
    campaign = models.ForeignKey(Campaign, blank = True)
    notes = models.TextField(max_length = 2047, blank = True)

    def __unicode__(self):
        return self.campaign.__unicode__()


class BusinessAsk(models.Model):
    """
    A request to a business for an in-kind gift
    """
    contacts = models.ManyToManyField('Business')
    date = models.DateField()
    campaign = models.ForeignKey(Campaign, blank = True)
    notes = models.TextField(max_length = 2047, blank = True)

    def __unicode__(self):
        return self.campaign.__unicode__()
