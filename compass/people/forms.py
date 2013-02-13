from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from crispy_forms.bootstrap import FormActions

from .models import Person


class ContactInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'street',
            'city',
            'state',
            'postcode',
            'country',
            'phone',
            'email',
            'facebook',
            'website',
            Submit('submit', 'Save'),
            )

        super(ContactInfoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Person
        fields = ('street',
                  'city',
                  'state',
                  'postcode',
                  'country',
                  'phone',
                  'email',
                  'facebook',
                  'website')

class PrivacyInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'public_profile', 'allow_compass_contact', 'allow_other_contact',
            Submit('submit', 'Save'),
            )
        super(PrivacyInfoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Person
        fields = ('public_profile', 'allow_compass_contact', 'allow_other_contact',)
