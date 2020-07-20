from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from . models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def my_products(request, name):
    user = User.objects.filter(username=name).first()
    product = Product.objects.filter(author=user).order_by('-date_posted')
    context = {'products':product}
    return render(request,'product/cardTest.html',context)

class ProductListView(ListView):
    model = Product
    template_name = 'product/cardTest.html'
    context_object_name = 'products'
    ordering = ['-date_posted']

def home(request):
    return render(request, 'product/home.html')

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'video_link', 'affiliate_link' ]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'video_link', 'affiliate_link' ]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url='/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False



def about(request):
    return render(request,'product/about.html')
