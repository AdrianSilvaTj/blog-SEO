from django.views.generic import (
    ListView
)
from django.shortcuts import render

class EntryListView(ListView):
    template_name = "entrada/list_all.html"
    context_object_name = 'entradas'
    paginate_by = 10
    

