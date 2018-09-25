from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.db.models import Q
from .models import Client, Employee
from price_list.models import PriceList
from cedis.models import Route
from sale.models import Order
from .forms import clientForm, employeeForm
from address.forms import addressForm, AddressFormSet
from django.forms import formset_factory
from address.models import Address
from cedis.models import Cedis

def LoginView(request):
    if not request.user.is_anonymous:
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    template_name = 'noactivo.html'
                    # no activo
                    return render(request, template_name, locals())
            else:
                # no usuario
                template_name = 'nousuario.html'
                return render(request, template_name, locals())
    else:
        formulario = AuthenticationForm()
    template_name = 'registration/login.html'
    return render(request, template_name, locals())


def LogoutView(request):
    logout(request)
    return redirect('index')


class PersonView(DetailView):
    model = Client
    template_name = 'client.html'

    def get(self, request, slug):
        self.client = get_object_or_404(Client, slug=self.kwargs['slug'])
        client = self.client
        route = client.route
        cedis = route.cedis
        orders = Order.objects.filter(client=self.client)
        address = Address.objects.filter(client=self.client)
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(createdAt__icontains=query)
            )
            results = Route.objects.filter(qset, client=self.client)
            template_name = "client.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())


class ClientCreation(View):
    model = Route
    form_class = clientForm
    initial = {'key': 'value'}
    template_name = 'form_client.html'
    Addres_FormSet=formset_factory(addressForm)

    def get(self, request, slug):
        page_title = 'Agregar cliente'
        self.route = get_object_or_404(Route, slug=self.kwargs['slug'])
        route = self.route
        cedis = route.cedis
        employee = Employee.objects.filter(cedis=route.cedis)
        price_list = PriceList.objects.filter(cedis=route.cedis)
        form = self.form_class(initial=self.initial)
        address_formset = AddressFormSet()
        return render(request, self.template_name, locals())

    def post(self, request, slug):
        self.route = get_object_or_404(Route, slug=self.kwargs['slug'])
        route = self.route        
        form = self.form_class(request.POST)
        address_formset = AddressFormSet(self.request.POST)
        person = Client.objects.all()
        if form.is_valid() and address_formset.is_valid():
            person = form.save(commit=False)
            person.save()
            address_formset.instance = person
            address_formset.save() 
            return redirect(route.get_absolute_url())
        else:
            form = self.form_class()
            address_formset = AddressFormSet()            
        args = {}
        # args.update(request)
        return render(request, self.template_name, locals())

class EmployeeCreation(View):
    model = Cedis
    form_class = employeeForm
    initial = {'key': 'value'}    
    template_name = 'form_employee.html'

    def get(self, request, slug):
        page_title = 'Agregar empleado'
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        cedis = self.cedis
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, locals())

    def post(self, request,slug):
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        cedis = self.cedis
        form = self.form_class(request.POST)
        employee = Employee.objects.all()
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect(cedis.get_absolute_url())
        else:
            form = self.routeForm() 
        args = {}
        #args.update(request)
        return render(request, self.template_name, locals())