from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from .models import Cedis, Route
from person.models import Client
from .forms import routeForm


from django.http import HttpResponse
from django.views import View

class IndexView(View):    
    template_name = 'index.html'

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        page_title = 'CaVe Logistics'
        return render(request, self.template_name, locals())


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

    # cedis = Cedis.objects.all()

    """def get_queryset(self):
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        return Route.objects.filter(cedis=self.cedis)"""


class RouteCreation(View):
    model = Cedis
    form_class = routeForm
    initial = {'key': 'value'}
    page_title = 'Agregar ruta'
    template_name = 'form_route.html'

    def get(self, request, slug):
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        cedis = self.cedis
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, locals())

    def post(self, request,slug):
        self.cedis = get_object_or_404(Cedis, slug=self.kwargs['slug'])
        cedis = self.cedis
        form = self.form_class(request.POST)
        route = Route.objects.all()
        if form.is_valid():
            route = form.save(commit=False)
            route.save()
            return redirect(cedis.get_absolute_url())
        else:
            form = self.routeForm() 
        args = {}
        #args.update(request)
        return render(request, self.template_name, locals())

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
