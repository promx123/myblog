from django.shortcuts import render
#
from django.views.generic import (
    ListView , DetailView ,  CreateView
)
# 
from django.urls import reverse_lazy , reverse

from .models import  Entry , Category

from .forms import  CrearEntradaForm

class  EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView,self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all() 
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get("kword",'')
        categoria = self.request.GET.get("categoria",'')
        #consulta de busqueda
        resultado = Entry.objects.buscar_entradas(kword , categoria)
        return resultado


class EntryDetailView(DetailView):
    model = Entry 
    template_name = "entrada/detail.html"
    
    
    
class CrearEntradaView(CreateView):
        template_name="entrada/crear_entrada.html"
        form_class= CrearEntradaForm
        success_url = reverse_lazy('entrada_app:entry-lista')
        
