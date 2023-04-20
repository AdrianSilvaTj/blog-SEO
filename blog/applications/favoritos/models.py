from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry

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
    
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('user','entry')
        
    def __str__(self):
        return self.entry.title
