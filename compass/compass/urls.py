from django.conf.urls import patterns, include, url

# Enable the admin
from django.contrib import admin
admin.autodiscover()

from .views import RegisterView, ManageView


urlpatterns = patterns('',
    url(r'^$', 'compass.views.home', name='home'),

    # urls for my applications
    url(r'^people/', include('people.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^finances/', include('finances.urls')),

    # TODO: put the admin at a hard-to-guess URL
    url(r'^admin/', include(admin.site.urls)),

    # for djtoken
    url(r"^djtokeninput/", include("djtokeninput.urls")),

    # for openid authentication
    url(r'^login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='openid-logout'),

    # put user registration & approval at the root
    url(r'^manage/$', ManageView.as_view(), name='manage'),
    url(r'^register/$', RegisterView.as_view(), name='register'),

)
