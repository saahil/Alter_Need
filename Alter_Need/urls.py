from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, login
from Alter_Need.have.views import profile, register, addLoc, addItem
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^have/', include('Alter_Need.have.urls')),
	(r'^', include('Alter_Need.need.urls')),
	(r'^accounts/login/$', login),
	(r'^accounts/logout/$', logout, {'next_page': "/have/"}),
	(r'^accounts/profile/$', profile),
	(r'^accounts/login/register/$', register),
    (r'^accounts/profile/addLoc/$', addLoc),
	(r'^accounts/profile/addItem/$', addItem),
	# Example:
    # (r'^Alter_Need/', include('Alter_Need.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
