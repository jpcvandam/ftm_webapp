"""ftm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls.static import static 
from django.conf.urls import include, url, patterns, handler404
from django.contrib import admin
import settings
from . import views

admin.autodiscover()
urlpatterns = patterns('ftm.views',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='ftm-index'),
    url(r'^grondwaterstand$', views.ftm, name='grondwaterstand'),
    url(r'^grondwaterstand-snel$', views.ftmsnel, name='grondwaterstand-snel'),
    url(r'^grondwaterstand-sql$', views.ftmsql, name='grondwaterstand-sql'),
    url(r'^download-reeks$', views.download_reeks)
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = views.page_not_found