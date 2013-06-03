from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy

import django_tables2 as tables

from compass.views import is_person, PersonRequiredMixin, LoginRequiredMixin, is_admin, MessageMixin
from .models import Person, CompassUser, Term, Role
from .forms import ContactInfoForm, PrivacyInfoForm, TermForm


class PersonTermTable(tables.Table):

    role = tables.LinkColumn("role_detail", args=[tables.utils.A("role.pk")])

    class Meta:
        model = Term
        exclude = ('id','person',)
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class ContactInfoUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):

    model = Person
    form_class = ContactInfoForm
    template_name = "people_update.html"
    success_url = reverse_lazy('people')
    success_message = "Contact information updated"

    def get_object(self, queryset = None):
        return self.request.user.person


class PrivacyInfoUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):

    model = Person
    form_class = PrivacyInfoForm
    template_name = "people_update.html"
    success_url = reverse_lazy('people')
    success_message = "Privacy settings updated"

    def get_object(self, queryset = None):
        return self.request.user.person


class PersonDetailView(PersonRequiredMixin, DetailView):
    model = Person
    template_name = "people_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)

        terms = Term.objects.filter(person=self.object)
        termtable = PersonTermTable(terms)
        tables.RequestConfig(self.request, paginate = False).configure(termtable)
        context['termtable'] = termtable
        return context


class PersonTable(tables.Table):
    name = tables.LinkColumn("person_detail", args=[tables.utils.A("pk")],
                             order_by=("first_name", "last_name"))

    class Meta:
        model = Person
        fields = ('name', 'content_type')
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class PersonListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Person
    table_class = PersonTable
    table_pagination = False
    template_name = "people_list.html"


@user_passes_test(is_person, login_url="/")
def search(request):
    return render(request, 'people_search.html')

class TermCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = Term
    form_class = TermForm
    template_name = 'people_update.html'
    success_url = "/people/"
    success_message = "Your term was created successfully"


class TermUpdateView(PersonRequiredMixin, MessageMixin,  UpdateView):
    model = Term
    form_class = TermForm
    template_name = 'people_update.html'
    success_url = "/people/"
    success_message = "Your term was updated successfully"

class RoleTable(tables.Table):

    title = tables.LinkColumn("role_detail", args=[tables.utils.A("pk")])

    class Meta:
        model = Role
        exclude = ('id',)
        attrs = {'class': 'table table-condensed table-hover table-bordered'}

class RoleListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Role
    table_class = RoleTable
    table_pagination = False
    template_name = "role_list.html"


class RoleTermTable(tables.Table):

    person = tables.LinkColumn("person_detail", args=[tables.utils.A("person.pk")])

    class Meta:
        model = Term
        exclude = ('id','role',)
        attrs = {'class': 'table table-condensed table-hover table-bordered'}

class RoleDetailView(PersonRequiredMixin, DetailView):
    model = Role
    template_name = "role_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RoleDetailView, self).get_context_data(**kwargs)
        terms = Term.objects.filter(role=self.object)
        termtable = RoleTermTable(terms)
        tables.RequestConfig(self.request, paginate = False).configure(termtable)
        context['termtable'] = termtable
        return context


@user_passes_test(is_person, login_url="/")
def index(request):

    terms = Term.objects.filter(role=request.user.person)
    termtable = PersonTermTable(terms)
    tables.RequestConfig(request, paginate = False).configure(termtable)

    return render(request, 'people_index.html', { 'termtable': termtable })
