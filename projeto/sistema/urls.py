from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sistema.core.views.home', name='home'),
    url(r'^profissionais/$', 'sistema.core.views.profissionais', name='profissionais'),
    url(r'^pacientes/$', 'sistema.core.views.pacientes', name='pacientes'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
