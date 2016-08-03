# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from failure import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin.site.urls),
    url(r'^awarie/$', 'failure.views.awarie'),
    url(r'^awarie_all/', 'failure.views.awarie_all'),

    url(r'^login/$', 'src.views.login'),
    url(r'^auth/$', 'src.views.auth_view'),
    url(r'^loggedin/$', 'src.views.loggedin'),
    url(r'^logout/$', 'src.views.logout'),
    url(r'^invalid/$', 'src.views.invalid_login'),

    url(r'^dashboard/$', 'src.views.dashboard'),
    url(r'^panel/$', 'src.views.panel'),
    
    url(r'^awarie_list/$', views.AwariaList.as_view(), name='awarie_list'),
    url(r'^new/$', views.AwariaCreate.as_view(), name='awaria_new'),
    url(r'^edit/(?P<pk>\d+)$', views.AwariaUpdate.as_view(), name='awaria_edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
