from django.conf.urls import url
from django.urls import path,re_path

from .views import (
    PersonView,
)
app_name = 'person'
urlpatterns = [

    path('<slug:slug>/', PersonView.as_view(), name='person_detail'),

]