from django.db import models
from people.models import Person


class Event(models.Model):

    LECTURE_SERIES = "LECTURE"
    OFFICE_HOURS = "OFFICE"
    COURSE = "COURSE"
    MEETING = "MEETING"
    FUNDRAISING = "FUNDING"
    SOCIAL = "SOCIAL"
    MENTORING = "MENTOR"
    OTHER ="OTHER"

    CATEGORY_CHOICES = (
        (LECTURE_SERIES, 'Lecture Series'),
        (OFFICE_HOURS, 'Office Hours'),
        (COURSE, 'Course'),
        (MEETING, 'Meeting'),
        (FUNDRAISING, 'Fundraising'),
        (SOCIAL, 'Social'),
        (MENTORING, 'Mentoring'),
        (OTHER, 'Other'),
        )

    # basic event data
    title = models.CharField(max_length = 255)
    date = models.DateField(auto_now_add = True)
    time = models.TimeField(auto_now_add = True)

    # more detailed information
    category = models.CharField(max_length = 15,
                                choices = CATEGORY_CHOICES)
    description = models.TextField(max_length = 4096, blank = True)

    # who was involved
    organizers = models.ManyToManyField(Person,
                                        related_name = "events_organized")
    attendees =  models.ManyToManyField(Person,
                                        related_name = "events_attended")

    def __unicode__(self):
        return self.title
