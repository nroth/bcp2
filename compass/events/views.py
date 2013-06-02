from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView

import django_tables2 as tables

from compass.views import PersonRequiredMixin, MessageMixin
from .models import Event
from .forms import EventForm

class EventCreateView(PersonRequiredMixin, MessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_create_form.html'
    success_url = "/events/"
    success_message = "Your event was created successfully"


class EventUpdateView(PersonRequiredMixin, MessageMixin,  UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_update_form.html'
    success_url = "/events/update/"
    success_message = "Your event was updated successfully"

    # def form_valid(self, form):
    #     r = super(EventUpdateView, self).form_valid(form)


class EventTable(tables.Table):

    title = tables.LinkColumn("event_detail", args=[tables.utils.A("pk")])

    class Meta:
        model = Event
        exclude = ('id', 'time', 'description',)
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class EventListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Event
    template_name = 'event_list.html'
    table_class = EventTable
    table_pagination = False

    def get_queryset(self):
        return self.request.user.person.events_attended.all()


class EventUpdateTable(PersonRequiredMixin, tables.Table):

    title = tables.LinkColumn("event_update", args=[tables.utils.A("pk")])

    class Meta:
        model = Event
        exclude = ('id', 'time', 'description',)
        attrs = {'class': 'table table-condensed table-hover table-bordered'}


class EventUpdateListView(PersonRequiredMixin, tables.SingleTableMixin, ListView):
    model = Event
    table_class = EventUpdateTable
    template_name = 'event_update_list.html'
    table_pagination = False

    def get_queryset(self):
        return self.request.user.person.events_organized.all()


class EventDetailView(PersonRequiredMixin, DetailView):
    model = Event
    template_name = 'event_detail.html'
