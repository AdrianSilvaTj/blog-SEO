""" Aca proporcionamos la estructura de nuestra web a buscacador para el SEO """

from django.contrib.sitemaps import Sitemap

from applications.entrada.models import Entry

class EntrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8 # prioridad del modelo en el sitio web 0 - 1
    protocol = 'https'
    
    def item(self):
        """ De donde generara las url para el esquema """
        return Entry.objects.filter(public=True)
    
    def lastmod(self, obj):
        return obj.created

class Sitemap(Sitemap):
    """ Esto lo pide django, es una regla """
    protocol = 'https'
    
    def __init__(self, names):
        self.names = names
        
    def item(self):
        return self.names
    
    def changefreq(self, obj):
        return 'weekly'