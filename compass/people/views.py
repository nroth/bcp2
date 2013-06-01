from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView, ListView, CreateView, UpdateView

import django_tables2 as tables

from compass.views import is_person, PersonRequiredMixin, LoginRequiredMixin, is_admin, MessageMixin
from .models import Person, CompassUser
from .forms import ContactInfoForm, PrivacyInfoForm


@user_passes_test(is_person, login_url="/")
def index(request):
    return render(request, 'people/index.html')


class ContactInfoUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):

    model = Person
    form_class = ContactInfoForm
    template_name = "update.html"
    success_url = "/"
    success_message = "Contact info updated"

    def get_object(self, queryset = None):
        return self.request.user.person


class PrivacyInfoUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):

    model = Person
    form_class = PrivacyInfoForm
    template_name = "update.html"
    success_url = "/"
    success_message = "Privacy info updated"

    def get_object(self, queryset = None):
        return self.request.user.person


class PersonDetailView(PersonRequiredMixin, DetailView):
    model = Person
    template_name = "detail.html"


class PersonTable(tables.Table):
    name = tables.LinkColumn("person_detail", args=[tables.utils.A("pk")],
                             order_by=("first_name", "last_name"))

    class Meta:
        model = Person
        fields = ('name', 'public_profile')
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class PersonListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Person
    table_class = PersonTable
    table_pagination = False
    template_name = "list.html"


@user_passes_test(is_person, login_url="/")
def search(request):
    return render(request, 'search.html')
