from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext 
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from .models import Client
from sale.models import Order


from django.http import HttpResponse
from django.views import View

class LiquidacionView(View):
	model = Order
	template_name = 'liquidacion.html'
	def get(self, request):
		cedis = Order.objects.all()		
		return render(request, self.template_name,locals())

class ClientRoute(DetailView):
	model = Order
	template_name = 'order.html'

	def get(self, request,slug):
		self.order = get_object_or_404(Order, slug=self.kwargs['slug'])
		order = self.order
		#clients = Client.objects.filter(=self.route)		
		return render(request, self.template_name,locals())
