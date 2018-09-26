from django.conf.urls import url
from django.urls import path,re_path

from .views import (
    CategoryView,
    ProductCategory,
    ProductDetail
)
app_name = 'product'
urlpatterns = [

    path('', CategoryView.as_view(), name='categorys'),
    #re_path(r'^nuevo$', CedisCreation.as_view(), name='new'),
    path('<slug:slug>/', ProductCategory.as_view(), name='category_detail'),
    #re_path(r'^nueva-ruta$', RouteCreation.as_view(), name='new_route'),
    #re_path(r'^(?P<slug>[\w-]+)/nueva-ruta/$', RouteCreation.as_view(), name='new_route'),
    #path('route/<slug:slug>/', ClientRoute.as_view(), name='route_detail'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),

]