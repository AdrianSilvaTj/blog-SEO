import datetime
from django.http import HttpResponseRedirect
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse,resolve

from django.views import View

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entry 
from .models import Home, Suscribers
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        # contexto de portada
        context['portada'] = Entry.objects.get_portada()
        # contexto de articulos en index.html
        context['home_entrys'] = Entry.objects.get_home_entrys()
        # contexto de acerca de nosotros
        context['home'] = Home.objects.latest('created')
        # contexto de articulos recientes
        context['rec_entrys'] = Entry.objects.get_recently_entrys()        
        return context

class SuscriberCreateView(View):
    """ Vista para guardar el correo del sucriptor, se llama en el formulario de suscribirse """
    
    def post(self, request, *args, **kwargs):
        """ Se utiliza para recuperar le valor del input del formulario """    
        print(request.POST['email'])
        Suscribers.objects.create(email = request.POST['email'])
        return HttpResponseRedirect(reverse('home_app:index'))
        
class ContactCreateView(CreateView):
    form_class = ContactForm
        
    def get_success_url(self):
        """ Se obtiene la url del template que en ese momento contiene al formulario y se
        retorna como la 'success_url' """
        container_url = self.request.META.get('HTTP_REFERER')       
        return container_url
    