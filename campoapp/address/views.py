from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import Location,Address
from .forms import addressForm
import json

class AutocomplateView(FormView):

	def get(self,request,*args,**kwargs):
	    q = self.request.GET.get('term','')
	    ret = []
	    listado = Location.objects.filter(name__istartswith=q).order_by("name")
	    for l in listado:
	        ret.append({'label':l.name + " / "+ l.municipality.state.short_name, 'value':l.id})
	        
	    return HttpResponse(json.dumps(ret), content_type='application/json')

class ClientAddressUpdate(View):
    model = Address
    form_class = addressForm
    initial = {'key': 'value'}
    template_name = 'form_edit_address.html'

    def get(self, request, id):
        page_title = 'Editar dirección'
        self.address = get_object_or_404(Address, id=self.kwargs['id'])
        address = self.address
        client = address.client
        route = client.route
        cedis = route.cedis
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, locals())

    def post(self, request, id):
        self.address = get_object_or_404(Address, id=self.kwargs['id'])
        address = self.address
        client = address.client
        route = client.route       
        form = self.form_class(request.POST,instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()            
            return redirect(client.get_absolute_url())
        else:
            form = self.form_class()         
        args = {}
        # args.update(request)
        return render(request, self.template_name, locals())