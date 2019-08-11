from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^home/',views.index),
    url(r'^search/$', views.getsearchdataview.as_view(),name='wordtext'),

]