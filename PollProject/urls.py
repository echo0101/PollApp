from django.conf.urls.defaults import patterns, include, url

from pollapp.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PollProject.views.home', name='home'),
    # url(r'^PollProject/', include('PollProject.foo.urls')),

		(r'^vote/(?P<pk>\d+)/$', vote),	
		(r'^vote/(?P<poll_pk>\d+)/(?P<keyword>\w+)/$', confirm),
		(r'^sms/$',smsVote),
		(r'^success/(?P<poll_pk>\d+)/(?P<choice_pk>\d+)/$', success),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

