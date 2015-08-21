from __future__ import absolute_import, unicode_literals

import os

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from feincms.module.page.sitemap import PageSitemap


sitemaps = {'pages': PageSitemap}

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media/')},
    ),

    url(
        r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps},
    ),

    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls')),
]

urlpatterns += staticfiles_urlpatterns()
