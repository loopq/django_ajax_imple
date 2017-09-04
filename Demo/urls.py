#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 18:35
# @Author  : zhuhu
# @DES     : 
# @File    : urls.py
# @Software: PyCharm



from django.conf.urls import url
from .views import *

app_name = 'demo'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^get/$', deal_get, name='deal_get'),
    url(r'^post/$', deal_post, name='deal_post'),
]
