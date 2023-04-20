from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """ Modelo para los favoritos """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='user_favorites'
        )
    entry = models.ForeignKey(
        Entry, 
        on_delete=models.CASCADE,
        related_name='entry_favorites'        
        )
    
    objects = FavoritesManager()
    
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('user','entry')
        
    def __str__(self):
        return str(self.id)+' - '+self.entry.title
