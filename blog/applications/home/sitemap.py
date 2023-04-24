""" Aca proporcionamos la estructura de nuestra web a buscacador para el SEO """
from datetime import timedelta, datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

from applications.entrada.models import Entry

class EntrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8 # prioridad del modelo en el sitio web 0 - 1
    protocol = 'https'
    
    def items(self):
        """ De donde generara las url para el esquema """
        return Entry.objects.filter(public=True)
    
    def lastmod(self, obj):
        return obj.created

class Sitemap(Sitemap):
    """ Esto lo pide django, es una regla """
    protocol = 'https'
    
    def __init__(self, names):
        self.names = names
        
    def items(self):
        return self.names
    
    def changefreq(self, obj):
        return 'weekly'
    
    def lastmod(self, obj):
        return datetime.now()
    
    def location(self, obj):
        return reverse_lazy(obj)
    