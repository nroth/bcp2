from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from people.models import CompassUser, Person


class RegisterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            Submit('submit', 'Confirm & Register'))
        super(RegisterForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = CompassUser
        fields = ('first_name', 'last_name')


class ManageForm(ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'person',            
            Submit('approve', 'Approve', css_class='btn-success'),
            Submit('deny', 'Deny',  css_class='btn-danger'),
            )
        super(ManageForm, self).__init__(*args, **kwargs)

        self.fields['person'].queryset = Person.objects.filter(compassuser__isnull=True)

        if not (self.instance.first_name and self.instance.last_name):
            name = "unknown"
        else:
            name = unicode(self.instance)
        self.fields['person'].label = "OpenID Name: {0}".format(name)
        
    class Meta:
        model = CompassUser
        fields = ('person',)
