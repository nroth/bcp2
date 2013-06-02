from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Role(models.Model):
    """
    A role might include being a student in a Compass class, being a
    cluster chair, or teaching for the summer program.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1023, blank = True)

    def __unicode__(self):
        return self.title


class Person(models.Model):
    """
    A person who has been involved in Compass.  The intent is that
    anyone who has ever identified as part of Compass will have at
    least a basic entry here.
    """

    # essential info
    name = models.CharField(max_length = 255, blank = True)

    # contact info
    street = models.CharField(max_length = 255, blank = True)
    city = models.CharField(max_length = 127, blank = True)
    state = models.CharField(max_length = 127, blank = True)
    postcode = models.CharField(max_length = 63, blank = True)
    country = models.CharField(max_length = 63, blank = True)
    phone = models.CharField(max_length = 63, blank = True)
    email = models.EmailField(max_length = 254, blank = True)

    # online presence
    facebook = models.URLField(blank = True)
    website = models.URLField(blank = True)

    # about
    about = models.TextField(blank = True)

    # privacy controls
    public_profile = models.BooleanField(
        "Other Compass students & alumni can view my profile",
        default = False)
    allow_compass_contact = models.BooleanField(
        "Compass can send me official communications (e.g. newsletter)",
        default = True)

    # roles
    roles = models.ManyToManyField(Role, through = 'Term')

    # last modified
    last_modified = models.DateTimeField(auto_now = True)

    # machinery to hook a person to a personaldata model
    # expect this to be Undergrad, Transfer, GradStudent, Postdoc
    content_type = models.ForeignKey(ContentType,
      limit_choices_to = {"model__in": ("undergrad", "transfer", "gradstudent", "postdoc")})
    object_id = models.PositiveIntegerField(blank = True, null = True)
    content_object = generic.GenericForeignKey()

    @classmethod
    def search(cls, query):
        return cls.objects.filter(name__icontains=query)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together   = ('content_type', 'object_id')
        verbose_name_plural = "People"


class PersonalData(models.Model):

    person = generic.GenericRelation(Person)

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        )

    sex = models.CharField(max_length=1, choices = SEX_CHOICES)
    ethnic_groups = models.CharField(max_length=255, blank = True)
    notes = models.TextField(max_length = 2047, blank = True)

    entered_cal_year = models.PositiveIntegerField(blank = True, null = True)
    joined_compass_year = models.PositiveIntegerField(blank = True, null = True)

    class Meta:
        abstract = True

    # def __unicode__(self):
    #     return self.person.get().name


class UGPersonalData(PersonalData):

    graduation_year = models.PositiveIntegerField(blank = True, null = True)
    major = models.CharField(max_length=255, blank = True)
    undergrad_research = models.CharField(max_length=255, blank = True)
    graduate_school = models.CharField(max_length=255, blank = True)

    class Meta:
        abstract = True


class Undergrad(UGPersonalData):
    """
    Data relevant for undergrads
    """

    household_income = models.PositiveIntegerField(blank = True, null = True)
    parental_degrees = models.CharField(max_length=255, blank = True)
    first_generation = models.NullBooleanField()

    class Meta:
        verbose_name = "Undergraduate Student"


class Transfer(UGPersonalData):
    """
    Data relevant for transfer students
    """

    previous_institution = models.CharField(max_length=255, blank = True)

    class Meta:
        verbose_name = "Transfer Student"


class GradStudent(PersonalData):
    """
    Data relevant for graduate students
    """

    ma_graduation_year = models.PositiveIntegerField(blank = True, null = True)
    phd_graduation_year = models.PositiveIntegerField(blank = True, null = True)
    department = models.CharField(max_length=255, blank = True)

    class Meta:
        verbose_name = "Graduate Student"

class Postdoc(models.Model):
    """
    Data relevant for graduate students
    """
    department = models.CharField(max_length=255, blank = True)

    class Meta:
        verbose_name = "Postdoctoral Researcher"


class Term(models.Model):
    """
    Connects a person and a role for a period of time.
    """

    person = models.ForeignKey(Person)
    role = models.ForeignKey(Role)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return "{0}: {1} - {2}".format(self.role, self.start_date, self.end_date)


class CompassUser(AbstractUser):
    """
    Extend the basic user model by allowing the association of a
    person with the user model.
    """

    person = models.OneToOneField(Person, blank = True, null = True)

    has_requested_person = models.BooleanField(default = False)

    objects = UserManager()

    def __unicode__(self):
        return " ".join((self.first_name, self.last_name))
