"""campoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from person import views

urlpatterns = [
    path('address/', include('address.urls')),
    path('cedis/', include('cedis.urls')),
    path('person/', include('person.urls')),
    path('liquidacion/', include('sale.urls')),
    path('ca/admin/', admin.site.urls),
    re_path(r'^login/$', views.LoginView, name='login'),
    re_path(r'^logout/$', views.LogoutView, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""if settings.DEBUG == False:
    urlpatterns += [
        path(r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT, }),
    ]"""
"""urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]"""
# Change admin site title
admin.site.site_header = "CAMPOAPP Administration"
admin.site.site_title = "CAMPOAPP Admin"
admin.site.index_title = "Welcome CAMPOAPP Administration"
