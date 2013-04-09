import csv
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, FormView
from django.db.models import Avg, Max, Min, Count, Sum
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import django_tables2 as tables
from django_tables2.utils import A
from django_tables2 import RequestConfig

from compass.views import PersonRequiredMixin, MessageMixin
from .forms import *
from .models import *


class BootstrapTable(tables.Table):

    def render_amount(self, value):
        return "%10.2f" % value

    def render_value(self, value):
        return "%10.2f" % value

    class Meta:
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class IndividualTable(BootstrapTable):

    name = tables.LinkColumn("individual_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = Individual
        fields = ('name',)


class IndividualAskTable(BootstrapTable):

    campaign = tables.LinkColumn("campaign_detail", args=[tables.utils.A("campaign.pk")])

    class Meta(BootstrapTable.Meta):
        model = IndividualAsk
        fields = ('date', 'campaign', 'notes')
        orderable = False


class SingleIndividualDonationTable(BootstrapTable):

    date = tables.LinkColumn("individualdonation_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = IndividualDonation
        fields = ('date', 'amount')
        orderable = False


class IndividualDonationTable(BootstrapTable):

    date = tables.LinkColumn("individualdonation_detail", args=[tables.utils.A("pk")])
    contact = tables.LinkColumn("individual_detail", args=[A("contact_id")])

    class Meta(BootstrapTable.Meta):
        model = IndividualDonation
        fields = ('date', 'contact', 'amount')


class IndividualCreateView(PersonRequiredMixin, CreateView):
    model = Individual
    form_class = IndividualForm
    template_name = "finances/individual_form.html"
    success_url = "/"


class IndividualListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Individual
    table_class = IndividualTable
    table_pagination = False


class IndividualDetailView(PersonRequiredMixin, DetailView):
    model = Individual

    def get_context_data(self, **kwargs):

        context = super(IndividualDetailView, self).get_context_data(**kwargs)

        donation_table = SingleIndividualDonationTable(self.object.individualdonation_set.all())
        ask_table = IndividualAskTable(self.object.individualask_set.all())

        tables.RequestConfig(self.request, paginate = False).configure(donation_table)
        tables.RequestConfig(self.request, paginate = False).configure(ask_table)

        context['donations'] = donation_table
        context['asks'] =  ask_table
        context['stats'] = self.object.individualdonation_set.all().aggregate(*[f('amount') for f in [Avg, Count, Min, Max, Sum]])

        return context


class IndividualUpdateView(PersonRequiredMixin, UpdateView):
    model = Individual
    form_class = IndividualForm
    template_name = "finances/individual_form.html"


class IndividualDonationCreateView(PersonRequiredMixin, CreateView):
    model = IndividualDonation
    form_class = IndividualDonationForm
    template_name = "finances/individualdonation_form.html"


class IndividualDonationDetailView(PersonRequiredMixin, DetailView):
    model = IndividualDonation


class IndividualDonationListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = IndividualDonation
    table_class = IndividualDonationTable
    table_pagination = False


class IndividualDonationUpdateView(PersonRequiredMixin, UpdateView):
    model = IndividualDonation
    form_class = IndividualDonationForm
    template_name = "finances/individualdonation_form.html"


class IndividualAskCreateView(PersonRequiredMixin, CreateView):
    model = IndividualAsk
    form_class = IndividualAskForm
    template_name = "finances/form.html"


class IndividualAskDetailView(PersonRequiredMixin, DetailView):
    model = IndividualAsk
    template_name = "finances/detail.html"


class IndividualAskListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = IndividualAsk
    table_class = IndividualAskTable
    table_pagination = False
    template_name = "finances/asklist.html"


class IndividualAskUpdateView(PersonRequiredMixin, UpdateView):
    model = IndividualAsk
    form_class = IndividualAskForm
    template_name = "finances/form.html"


class BusinessTable(BootstrapTable):

    name = tables.LinkColumn("business_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = Business
        fields = ('name',)


class BusinessAskTable(BootstrapTable):

    campaign = tables.LinkColumn("campaign_detail", args=[tables.utils.A("campaign.pk")])

    class Meta(BootstrapTable.Meta):
        model = BusinessAsk
        fields = ('date', 'campaign', 'notes')
        orderable = False


class SingleBusinessDonationTable(BootstrapTable):

    date = tables.LinkColumn("businessdonation_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = BusinessDonation
        fields = ('date', 'value')
        orderable = False


class BusinessDonationTable(BootstrapTable):

    date = tables.LinkColumn("businessdonation_detail", args=[tables.utils.A("pk")])
    contact = tables.LinkColumn("business_detail", args=[A("contact_id")])

    class Meta(BootstrapTable.Meta):
        model = BusinessDonation
        fields = ('date', 'contact', 'value')


class BusinessCreateView(PersonRequiredMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = "finances/form.html"


class BusinessListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Business
    table_class = BusinessTable
    table_pagination = False


class BusinessDetailView(PersonRequiredMixin, DetailView):
    model = Business

    def get_context_data(self, **kwargs):

        context = super(BusinessDetailView, self).get_context_data(**kwargs)

        donation_table = SingleBusinessDonationTable(self.object.businessdonation_set.all())
        ask_table = BusinessAskTable(self.object.businessask_set.all())

        tables.RequestConfig(self.request, paginate = False).configure(donation_table)
        tables.RequestConfig(self.request, paginate = False).configure(ask_table)

        context['donations'] = donation_table
        context['asks'] =  ask_table
        context['stats'] = self.object.businessdonation_set.all().aggregate(*[f('value') for f in [Avg, Count, Min, Max, Sum]])

        print(context['stats'])
        return context


class BusinessUpdateView(PersonRequiredMixin, UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = "finances/form.html"


class BusinessDonationCreateView(PersonRequiredMixin, CreateView):
    model = BusinessDonation
    form_class = BusinessDonationForm
    template_name = "finances/form.html"


class BusinessDonationDetailView(PersonRequiredMixin, DetailView):
    model = BusinessDonation
    template_name = "finances/detail.html"


class BusinessDonationListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = BusinessDonation
    table_class = BusinessDonationTable
    table_pagination = False
    template_name = "finances/donationlist.html"


class BusinessDonationUpdateView(PersonRequiredMixin, UpdateView):
    model = BusinessDonation
    form_class = BusinessDonationForm
    template_name = "finances/form.html"


class BusinessAskCreateView(PersonRequiredMixin, CreateView):
    model = BusinessAsk
    form_class = BusinessAskForm
    template_name = "finances/form.html"


class BusinessAskDetailView(PersonRequiredMixin, DetailView):
    model = BusinessAsk
    template_name = "finances/detail.html"


class BusinessAskListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = BusinessAsk
    table_class = BusinessAskTable
    table_pagination = False
    template_name = "finances/asklist.html"


class BusinessAskUpdateView(PersonRequiredMixin, UpdateView):
    model = BusinessAsk
    form_class = BusinessAskForm
    template_name = "finances/form.html"


class CampaignTable(BootstrapTable):

    name = tables.LinkColumn("campaign_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = Individual
        fields = ('name','start_date', 'end_date')


class CampaignListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Campaign
    table_class = CampaignTable
    table_pagination = False
    template_name = "finances/list.html"


class CampaignCreateView(PersonRequiredMixin, CreateView):
    model = Campaign
    template_name = "finances/form.html"


class CampaignDetailView(PersonRequiredMixin, DetailView):
    model = Campaign

    def get_context_data(self, **kwargs):

        context = super(CampaignDetailView, self).get_context_data(**kwargs)

        individual_ask_table = IndividualAskTable(self.object.individualask_set.all())
        business_ask_table = BusinessAskTable(self.object.businessask_set.all())

        tables.RequestConfig(self.request, paginate = False).configure(business_ask_table)
        tables.RequestConfig(self.request, paginate = False).configure(individual_ask_table)

        context['individual_asks'] = individual_ask_table
        context['business_asks'] = business_ask_table

        return context


class CampaignUpdateView(PersonRequiredMixin, UpdateView):
    model = Campaign
    template_name = "finances/form.html"



def home(request):

    recent_individual_donations = IndividualDonationTable(IndividualDonation.objects.order_by('-pk')[:10])
    recent_business_donations = BusinessDonationTable(BusinessDonation.objects.order_by('-pk')[:10])

    RequestConfig(request, paginate = False).configure(recent_individual_donations)
    RequestConfig(request, paginate = False).configure(recent_business_donations)

    return render(request, 'finances/index.html',
                  {'recent_individual': recent_individual_donations,
                   'recent_business': recent_business_donations})


class IndividualSearchFormView(PersonRequiredMixin, FormView):
    template_name = "finances/search.html"
    form_class = IndividualSearchForm

    def form_valid(self, form):

        # do search
        query  = Individual.objects.all()
        # generate table
        results_table = IndividualTable(query)

        if "download" in self.request.POST:
            response = HttpResponse(mimetype='text/csv')
            response['Content-Disposition'] = 'attachment;filename="gifts_search.csv"'
            writer = csv.writer(response)
            writer.writerow(["name","street", "city", "state",
                             "postcode", "country", "email"])
            for contact in query:
                writer.writerow([contact.name,
                                 contact.street,
                                 contact.city,
                                 contact.state,
                                 contact.postcode,
                                 contact.country,
                                 contact.email])
            return response


        elif "newask" in self.request.POST and query:
            newask = IndividualAsk(date = datetime.date.today(),
                                   campaign = Campaign.objects.get(pk=1))
            newask.save()
            for contact in query:
                newask.contacts.add(contact)
                newask.save()
            edit_url = reverse('individualask_update', kwargs={'pk': newask.pk})
            return HttpResponseRedirect(edit_url)


        RequestConfig(self.request, paginate = False).configure(results_table)

        return render(self.request, self.template_name, {'form':form,
                                                         'table': results_table})
