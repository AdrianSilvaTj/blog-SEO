from django.db import models

class EntryManager(models.Manager):
    """ Manager para Entry """
    def get_portada(self):
        """ devuelve el articulo en portada """
        return self.filter(
            public = True,
            portada = True
        ).order_by('-created').first()
        
    def get_home_entrys(self):
        """ devuelve las ultimas 4 entradas que van al home """
        return self.filter(
            public = True,
            in_home = True,
            portada = False
        ).order_by('-created')[:4]
        
    def get_recently_entrys(self):
        """ devuelve las 6 entradas mas recientes """
        return self.filter(
            public = True,            
        ).order_by('-created')[:6]
        
    def entry_search(self,kword, category):
        if len(category) > 0:
            return self.filter(
                category__short_name = category,
                title__icontains = kword,
                public= True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains = kword,
                public= True
            ).order_by('-created')