from django.conf.urls import url
from django.urls import path,re_path

from .views import (
    LiquidacionView,
)
app_name = 'sale'
urlpatterns = [

    path('', LiquidacionView.as_view(), name='liquidacion_detail'),

]