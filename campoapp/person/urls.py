from django.urls import path, re_path

from .views import (
    PersonView, 
    LoginView, 
    LogoutView,
)
app_name = 'person'
urlpatterns = [

    path('<slug:slug>/', PersonView.as_view(), name='person_detail'),
    

]
