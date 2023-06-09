from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.views.generic import (
    ListView,
    View,
    DeleteView
)
from applications.entrada.models import Entry
from .models import Favorites


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    success_url ='.'
    login_url = reverse_lazy('users_app:user-login')
    
    def get_queryset(self):
        return Favorites.objects.entrys_user(self.request.user)
    
class AddFavoritesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')
    
    def post(self, request, *args, **kwargs):
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        print(self.kwargs)
        
        Favorites.objects.create(
            user = usuario,
            entry = entrada
        )
        
        return HttpResponseRedirect(reverse('favoritos_app:perfil'))
    
class FavoritesDeleteView(DeleteView):
    model=Favorites
    success_url = reverse_lazy('favoritos_app:perfil')