from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$',
        "finances.views.home",
        name='finances'),
    url(r'^search/$',
        IndividualSearchFormView.as_view(),
        name='donation_search'),

    url(r'^individual/$',
        IndividualListView.as_view(),
        name = 'individual_list'),
    url(r'^individual/new$',
        IndividualCreateView.as_view(),
        name = 'individual_create'),
    url(r'^individual/(?P<pk>\d+)/$',
        IndividualDetailView.as_view(),
        name = 'individual_detail'),
    url(r'^individual/edit/(?P<pk>\d+)/$',
        IndividualUpdateView.as_view(),
        name = 'individual_update'),

    url(r'^donations/individual/$',
        IndividualDonationListView.as_view(),
        name = 'individualdonation_list'),
    url(r'^donations/individual/new$',
        IndividualDonationCreateView.as_view(),
        name = 'individualdonation_create'),
    url(r'^donations/individual/(?P<pk>\d+)/$',
        IndividualDonationDetailView.as_view(),
        name = 'individualdonation_detail'),
    url(r'^donations/individual/edit/(?P<pk>\d+)/$',
        IndividualDonationUpdateView.as_view(),
        name = 'individualdonation_update'),

    url(r'^asks/individual/$',
        IndividualAskListView.as_view(),
        name = 'individualask_list'),
    url(r'^asks/individual/new$',
        IndividualAskCreateView.as_view(),
        name = 'individualask_create'),
    url(r'^asks/individual/(?P<pk>\d+)/$',
        IndividualAskDetailView.as_view(),
        name = 'individualask_detail'),
    url(r'^asks/individual/edit/(?P<pk>\d+)/$',
        IndividualAskUpdateView.as_view(),
        name = 'individualask_update'),

    url(r'^business/$',
        BusinessListView.as_view(),
        name = 'business_list'),
    url(r'^business/new$',
        BusinessCreateView.as_view(),
        name = 'business_create'),
    url(r'^business/(?P<pk>\d+)/$',
        BusinessDetailView.as_view(),
        name = 'business_detail'),
    url(r'^business/edit/(?P<pk>\d+)/$',
        BusinessUpdateView.as_view(),
        name = 'business_update'),

    url(r'^donations/business/$',
        BusinessDonationListView.as_view(),
        name = 'businessdonation_list'),
    url(r'^donations/business/new$',
        BusinessDonationCreateView.as_view(),
        name = 'businessdonation_create'),
    url(r'^donations/business/(?P<pk>\d+)/$',
        BusinessDonationDetailView.as_view(),
        name = 'businessdonation_detail'),
    url(r'^donations/business/edit/(?P<pk>\d+)/$',
        BusinessDonationUpdateView.as_view(),
        name = 'businessdonation_update'),

    url(r'^asks/business/$',
        BusinessAskListView.as_view(),
        name = 'businessask_list'),
    url(r'^asks/business/new$',
        BusinessAskCreateView.as_view(),
        name = 'businessask_create'),
    url(r'^asks/business/(?P<pk>\d+)/$',
        BusinessAskDetailView.as_view(),
        name = 'businessask_detail'),
    url(r'^asks/business/edit/(?P<pk>\d+)/$',
        BusinessAskUpdateView.as_view(),
        name = 'businessask_update'),

    url(r'^campaign/$',
        CampaignListView.as_view(),
        name = 'campaign_list'),
    url(r'^campaign/new$',
        CampaignCreateView.as_view(),
        name = 'campaign_create'),
    url(r'^campaign/(?P<pk>\d+)/$',
        CampaignDetailView.as_view(),
        name = 'campaign_detail'),
    url(r'^update/$',
        CampaignUpdateListView.as_view(),
        name = 'campaigns_update'),
    url(r'^update/(?P<pk>\d+)/$', CampaignUpdateView.as_view(),
        name = 'campaign_update'),

)
