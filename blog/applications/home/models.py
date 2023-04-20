from django.db import models
from model_utils.models import TimeStampedModel

# Utilizamos 'TimeStampedModel', ya que agrega algunas funcionalidades como tener 
# la fecha de creación y de modificación del modelo
class Home(TimeStampedModel):
    """ Modelo para la pagina principal """
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('Email de Contacto', blank=True, null=True)
    phone = models.CharField('Telefono de Contacto', max_length=20)
    
    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
        
    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    """ Modelo para Suscriptores """
    email = models.EmailField('Email')
    
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
    """ Modelo para los contactos """
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField('Email')
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.full_name
