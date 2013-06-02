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


class IndividualCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = Individual
    form_class = IndividualForm
    template_name = "individual_form.html"
    success_url = "/finances/individual/"
    success_message = "Individual info created successfully"


class IndividualListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Individual
    template_name = "individual_list.html"
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


class IndividualUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = Individual
    form_class = IndividualForm
    template_name = "individual_form.html"
    success_url = "/finances/individual/"
    success_message = "Individual info updated successfully"


class IndividualDonationCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = IndividualDonation
    form_class = IndividualDonationForm
    template_name = "individualdonation_form.html"
    success_url = "/finances/donations/individual/"
    success_message = "Donation info created successfully"


class IndividualDonationDetailView(PersonRequiredMixin, DetailView):
    model = IndividualDonation

class IndividualDonationListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = IndividualDonation
    table_class = IndividualDonationTable
    table_pagination = False

class IndividualDonationUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = IndividualDonation
    form_class = IndividualDonationForm
    template_name = "individualdonation_form.html"
    success_url = "/finances/donations/individual/"
    success_message = "Donation info updated successfully"


class IndividualAskCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = IndividualAsk
    form_class = IndividualAskForm
    template_name = "form.html"
    success_url = "/finances/individual/"
    success_message = "Ask info created successfully"


class IndividualAskDetailView(PersonRequiredMixin, DetailView):
    model = IndividualAsk
    template_name = "detail.html"


class IndividualAskListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = IndividualAsk
    table_class = IndividualAskTable
    table_pagination = False
    template_name = "asklist.html"


class IndividualAskUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = IndividualAsk
    form_class = IndividualAskForm
    template_name = "form.html"
    success_url = "/finances/"
    success_message = "Ask info updated successfully"


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


class BusinessCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Business info created successfully"


class BusinessListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Business
    template_name = "business_list.html"
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

        return context


class BusinessUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Business info updated successfully"


class BusinessDonationCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = BusinessDonation
    form_class = BusinessDonationForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Donation info created successfully"



class BusinessDonationDetailView(PersonRequiredMixin, DetailView):
    model = BusinessDonation
    template_name = "detail.html"


class BusinessDonationListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = BusinessDonation
    table_class = BusinessDonationTable
    table_pagination = False
    template_name = "donationlist.html"


class BusinessDonationUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = BusinessDonation
    form_class = BusinessDonationForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Donation info updated successfully"


class BusinessAskCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = BusinessAsk
    form_class = BusinessAskForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Ask info created successfully"

class BusinessAskDetailView(PersonRequiredMixin, DetailView):
    model = BusinessAsk
    template_name = "detail.html"


class BusinessAskListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = BusinessAsk
    table_class = BusinessAskTable
    table_pagination = False
    template_name = "asklist.html"


class BusinessAskUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = BusinessAsk
    form_class = BusinessAskForm
    template_name = "form.html"
    success_url = "/finances/business/"
    success_message = "Ask info updated successfully"


class CampaignTable(BootstrapTable):

    name = tables.LinkColumn("campaign_detail", args=[tables.utils.A("pk")])

    class Meta(BootstrapTable.Meta):
        model = Individual
        fields = ('name','start_date', 'end_date')


class CampaignListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Campaign
    table_class = CampaignTable
    table_pagination = False
    template_name = "list.html"


class CampaignCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = "form.html"
    success_url = "/finances/"
    success_message = "Campaign info created sucessfully"


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


class CampaignUpdateView(PersonRequiredMixin, MessageMixin, UpdateView):
    model = Campaign
    template_name = "form.html"
    success_url = "/finances/"
    success_message = "Campaign info updated sucessfully"



def home(request):

    recent_individual_donations = IndividualDonationTable(IndividualDonation.objects.order_by('-pk')[:10])
    recent_business_donations = BusinessDonationTable(BusinessDonation.objects.order_by('-pk')[:10])

    RequestConfig(request, paginate = False).configure(recent_individual_donations)
    RequestConfig(request, paginate = False).configure(recent_business_donations)

    return render(request, 'finances_index.html',
                  {'recent_individual': recent_individual_donations,
                   'recent_business': recent_business_donations})


class IndividualSearchFormView(PersonRequiredMixin, FormView):
    template_name = "search.html"
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
