from django.conf.urls import patterns, include, url
from events.views import *

urlpatterns = patterns('',
    url(r'^$', EventListView.as_view(), name='events'),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(),name = 'event_detail'),
    url(r'^create/$',EventCreateView.as_view(),name = 'event_create'),
    url(r'^update/$', EventUpdateListView.as_view(), name='events_update'),
    url(r'^update/(?P<pk>\d+)/$', EventUpdateView.as_view(),
        name = 'event_update'),
)
