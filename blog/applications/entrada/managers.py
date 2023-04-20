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