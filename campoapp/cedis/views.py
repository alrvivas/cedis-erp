from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from .models import Cedis, Route
from person.models import Client


from django.http import HttpResponse
from django.views import View



class CedisView(View):
    model = Cedis
    page_title = 'CEDIS'
    template_name = 'cedis.html'

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        cedis = Cedis.objects.all()
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(name__icontains=query)
            )
            results = Cedis.objects.filter(qset)
            template_name = "cedis.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())


class CedisCreation(CreateView):
    model = Cedis
    page_title = 'Agregar CEDIS'
    template_name = 'form_cedis.html'
    success_url = reverse_lazy('cedis:cedis')
    fields = ('__all__')


class RouteCedis(DetailView):

    model = Cedis
    template_name = 'routes.html'

    def get(self, request, slug):
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        routes = Route.objects.filter(cedis=self.cedis)
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(name__icontains=query)
            )
            results = Route.objects.filter(qset, cedis=self.cedis)
            template_name = "cedis.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())

    #cedis = Cedis.objects.all()

    """def get_queryset(self):
		self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
		return Route.objects.filter(cedis=self.cedis)"""


class RouteCreation(CreateView, View):
    model = Route
    page_title = 'Agregar ruta'
    template_name = 'form_route.html'
    success_url = reverse_lazy('cedis:cedis_detail')
    fields = ('__all__')


class ClientRoute(DetailView):
    model = Route
    template_name = 'route_clients.html'

    def get(self, request, slug):
        self.route = get_object_or_404(Route, slug=self.kwargs['slug'])
        route = self.route
        clients = Client.objects.filter(route=self.route)
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(name__icontains=query)
            )
            results = Client.objects.filter(qset, route=self.route)
            template_name = "route_clients.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())
