from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from djtokeninput import TokenField, TokenWidget

from .models import *


class IndividualSearchForm(forms.Form):
    """Simple form to search contacts based on donations/asks"""

    # what about people who don't have these records
    show_non_donors = forms.BooleanField(required = False)
    show_never_asked = forms.BooleanField(required = False)

    #amount_operator = 0 # and / or
    #amount_type = 0 # all / one / none

    # range of donation amounts
    amount_min = forms.DecimalField(max_digits = 12, decimal_places = 2, required = False)
    amount_max = forms.DecimalField(max_digits = 12, decimal_places = 2, required = False)

    # if you want to set the date field to have a dropdown with a
    # range of donation dates: allow 2007 - current year
    # set the forms.DateField(widget = widget), where
    # year_range = range(2007, datetime.date.today().year + 1)
    # widget = SelectDateWidget(years = year_range)

    donate_date_operator = forms.ChoiceField(choices=(("AND","AND"),("OR","OR")),
                                             widget=forms.RadioSelect)
    donate_date_type = forms.ChoiceField(choices=(("ALL","ALL"),("ONE", "ONE"),("NONE", "NONE")))

    donate_date_min = forms.DateField(required = False)
    donate_date_max = forms.DateField(required = False)

    # range of ask dates
    ask_date_operator = forms.ChoiceField(choices=(("AND","AND"),("OR","OR")),
                                          widget=forms.RadioSelect)
    ask_date_type = forms.ChoiceField(choices=(("ALL","ALL"),("ONE", "ONE"),("NONE", "NONE")))

    ask_date_min = forms.DateField(required = False)
    ask_date_max = forms.DateField(required = False)

    # require contact information
    has_email = forms.BooleanField(required = False)
    has_address = forms.BooleanField(required = False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Donation Date Information',
                     'donate_date_operator',
                     'donate_date_type',
                     'donate_date_min',
                     'donate_date_max'),
            Fieldset('Ask Date Information',
                     'ask_date_operator',
                     'ask_date_type',
                     'ask_date_min',
                     'ask_date_max'),
            Submit('submit', 'Search'),
            Submit('download', 'Download'),
            Submit('newask', 'New Ask'),
        )
        super(IndividualSearchForm, self).__init__(*args, **kwargs)



class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(IndividualForm, self).__init__(*args, **kwargs)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(BusinessForm, self).__init__(*args, **kwargs)


class IndividualAskForm(forms.ModelForm):

    contacts = TokenField(Individual,
                          widget=TokenWidget(
            hint_text="Add/Remove Contants",
            prevent_duplicates = True,
            animate_dropdown=False))

    class Meta:
        model = IndividualAsk

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(IndividualAskForm, self).__init__(*args, **kwargs)


class BusinessAskForm(forms.ModelForm):

    contacts = TokenField(Business,
                          widget=TokenWidget(
            hint_text="Add/Remove Contants",
            prevent_duplicates = True,
            animate_dropdown=False))

    class Meta:
        model = BusinessAsk

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(BusinessAskForm, self).__init__(*args, **kwargs)


class IndividualDonationForm(forms.ModelForm):

    class Meta:
        model = IndividualDonation

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(IndividualDonationForm, self).__init__(*args, **kwargs)


class BusinessDonationForm(forms.ModelForm):
    class Meta:
        model = BusinessDonation

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(BusinessDonationForm, self).__init__(*args, **kwargs)

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(CampaignForm, self).__init__(*args, **kwargs)
