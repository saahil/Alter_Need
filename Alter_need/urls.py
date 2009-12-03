from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, login
from Alter_Need.have.views import profile, register
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^have/', include('Alter_Need.have.urls')),
	(r'^accounts/login/$', login),
	(r'^accounts/logout/$', logout),
	(r'^accounts/profile/$', profile),
	(r'^accounts/login/register/$', register),
    # Example:
    # (r'^Alter_Need/', include('Alter_Need.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
