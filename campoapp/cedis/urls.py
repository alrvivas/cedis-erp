from django.conf.urls import url
from django.urls import path,re_path

from .views import (
    CedisView,
    CedisCreation,
    RouteCedis,
    RouteCreation,
    ClientRoute,
)
app_name = 'cedis'
urlpatterns = [

    path('', CedisView.as_view(), name='cedis'),
    re_path(r'^nuevo$', CedisCreation.as_view(), name='new'),
    path('<slug:slug>/', RouteCedis.as_view(), name='cedis_detail'),
    re_path(r'^nueva-ruta$', RouteCreation.as_view(), name='new_route'),
    path('route/<slug:slug>/', ClientRoute.as_view(), name='route_detail'),
    #re_path(r'^(?P<slug:slug>[-\w]+)/$', RouteCedis.as_view(), name='cedis_detail'),

]