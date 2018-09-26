from django.urls import path, re_path

from .views import (
    PersonView, 
    LoginView, 
    LogoutView,
    ClientCreation,
    EmployeeCreation,
    ClientUpdate
)
app_name = 'person'
urlpatterns = [

    path('<slug:slug>/', PersonView.as_view(), name='person_detail'),
    re_path(r'^(?P<slug>[\w-]+)/nuevo-cliente/$', ClientCreation.as_view(), name='new_client'),
    re_path(r'^(?P<slug>[\w-]+)/editar-cliente/$', ClientUpdate.as_view(), name='update_client'),
    re_path(r'^(?P<slug>[\w-]+)/nuevo-empleado/$', EmployeeCreation.as_view(), name='new_employee'),    

]
