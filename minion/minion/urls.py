"""minion URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
import ajax_import
import ajax_update_users

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/import/$', ajax_import.import_garden_data, name='ajax_import'),
    url(r'^update_users/$', ajax_update_users.import_user_data, name='update_users'),
    url(r'^search_criteria/update_users/$', ajax_update_users.import_user_data, name='update_users'),
    url(r'',include('garden.urls')),
    #twitterauth
    url('', include('social.apps.django_app.urls', namespace='social')),
]
