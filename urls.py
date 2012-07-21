from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout, password_change,password_change_done
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ads.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_adservice.views.home', name='home'),
    # url(r'^my_adservice/', include('my_adservice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    (r'^accounts/login/$',  login),
(r'^accounts/logout/$', logout),
(r'^accounts/password/change/$',password_change),
(r'accounts/password/done/$', password_change_done),
(r'^$',home),

)
