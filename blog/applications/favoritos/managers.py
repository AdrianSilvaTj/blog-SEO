from django.db import models

class FavoritesManager(models.Manager):
    
    def entrys_user(self, usuario):
        return self.filter(
            user = usuario,
            entry__public = True
        ).order_by('-created')