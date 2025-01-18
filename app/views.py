from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name= 'produtos_list.html'
    context_object_name = 'products'
    paginate_by = 10

#CRUD

#CREATE
class ProductCreateView(CreateView):
    model = Product
    fields = ['name','image','brand','category','description','price','countInStock','user']
    template_name = "product_create_update.html"
    success_url = reverse_lazy('product-list')


#READ
class ProductDetailView(DetailView):
    model = Product
    template_name = "produtos_detail.html"
    context_object_name = 'product'

#UPDATE
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','image','brand','category','description','price','countInStock','user']
    template_name = "product_create_uptade.html"
    success_url = reverse_lazy('product-list')


#DELETE
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy('product-list')
