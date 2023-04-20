from django.views.generic import (
    ListView, DetailView
)
from django.shortcuts import render

from .models import Entry, Category

class EntryListView(ListView):
    template_name = "entrada/list_all.html"
    context_object_name = 'entrys'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        category = self.request.GET.get('category','')
        # consulta de busqueda
        result = Entry.objects.entry_search(kword, category)
        return result


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
