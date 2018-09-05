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
from .models import Location
import json

class AutocomplateView(FormView):

	def get(self,request,*args,**kwargs):
	    q = self.request.GET.get('term','')
	    ret = []
	    listado = Location.objects.filter(name__istartswith=q).order_by("name")
	    for l in listado:
	        ret.append({'label':l.name + " / "+ l.municipality.state.short_name, 'value':l.id})
	        
	    return HttpResponse(json.dumps(ret), content_type='application/json')