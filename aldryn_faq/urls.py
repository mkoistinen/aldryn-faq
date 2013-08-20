# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_faq.views import FaqByCategoryView, FaqAnswerView

urlpatterns = patterns(
    '',
    url(r'^(?P<category_slug>[-\w]+)/$', FaqByCategoryView.as_view(), name='faq-category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<id>[0-9]+)$', FaqAnswerView.as_view(), name='faq-answer'),
)
