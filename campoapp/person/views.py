from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.db.models import Q
from .models import Client
from cedis.models import Route
from sale.models import Order


from django.http import HttpResponse
from django.views import View


def LoginView(request):
    if not request.user.is_anonymous:
        return redirect('cedis:cedis')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('cedis:cedis')
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
    return redirect('cedis:cedis')


class PersonView(DetailView):
    model = Client
    template_name = 'client.html'

    def get(self, request, slug):
        self.client = get_object_or_404(Client, slug=self.kwargs['slug'])
        client = self.client
        orders = Order.objects.filter(client=self.client)
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
