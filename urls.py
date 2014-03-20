from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'university.views.home', name='home'),
    # url(r'^university/', include('university.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    #(r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^students/$', 'student.views.StudentsAll'),
    (r'^students/(?P<studentslug>.*)/$', 'student.views.SpecificStudent'),
    (r'^modules/(?P<moduleslug>.*)/$', 'student.views.SpecificModule'),
)
