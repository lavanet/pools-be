from django.urls import re_path as url

from . import views

__author__ = 'snake'

urlpatterns = [
    url('^$', views.template_list, name='email_template_list'),
    url('^(?P<pk>.+?)/$', views.template_single, name='email_template_single'),
]
