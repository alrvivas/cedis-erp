from django.conf.urls import url
from django.urls import path,re_path

from .views import (
    AutocomplateView,
)
app_name = 'address'
urlpatterns = [

    re_path(r'^autocomplate-location/$', AutocomplateView.as_view(), name='autocomplate_location'),

]