from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from .models import Product, Category
from person.models import Client

class CategoryView(View):
    model = Category    
    template_name = 'categorys.html'

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        category = Category.objects.all()
        page_title = 'Categorías'
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(name__icontains=query)
            )
            results = Category.objects.filter(qset)
            template_name = "categorys.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())

class ProductCategory(DetailView):

    model = Category    
    template_name = 'products.html'

    def get(self, request, slug):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        category = self.category
        page_title = category.name
        products = Product.objects.filter(category=self.category)
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(name__icontains=query)
            )
            results = Product.objects.filter(qset, category=self.category)
            template_name = "category.html"
            return render(request, self.template_name, locals())
        else:
            results = []
        return render(request, self.template_name, locals())

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'

    def get(self, request, slug):
        self.product = get_object_or_404(Product, slug=self.kwargs['slug'])
        product = self.product
        page_title = product.name
        category = product.category        
        return render(request, self.template_name, locals())