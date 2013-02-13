from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from djtokeninput import TokenField, TokenWidget

from people.models import Person
from .models import Event


class EventForm(ModelForm):

    organizers = TokenField(Person,
                            required=False,
                            widget=TokenWidget(
            hint_text="Add/Remove Organizers",
            prevent_duplicates=True,
            animate_dropdown=False))


    attendees = TokenField(Person,
                            required=False,
                            widget=TokenWidget(
            hint_text="Add/Remove Attendees",
            prevent_duplicates=True,
            animate_dropdown=False))


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(EventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Event
