from django.shortcuts import render
from .models import Store
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    products = Store.objects.all().order_by('-date_posted')
    context = {'products':products}
    return render(request, 'store/home.html', context)

def mystore(request, name):
    user = User.objects.filter(username=name).first()
    product = Store.objects.filter(author=user).order_by('-date_posted')
    context = {'products':product}
    return render(request,'store/home.html',context)


class StoreDetailView( DetailView):
    model = Store


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['title', 'description', 'image', 'affiliate_link', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoreDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Store
    success_url = '/store/'

    def test_func(self):
        store = self.get_object()
        if store.author == self.request.user:
            return True
        return False


class StoreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['title', 'description', 'image', 'affiliate_link', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        store = self.get_object()
        if store.author == self.request.user:
            return True
        return False
