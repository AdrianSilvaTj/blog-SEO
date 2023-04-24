from datetime import timedelta, datetime

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import EntryManager

class Category(TimeStampedModel):
    """ Modelo para Categorias """
    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)
        
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """ Modelo para las etiquetas """
    name = models.CharField('Nombre', max_length=30)
    
    class Meta:
        verbose_name = 'Etiqueta/Tag'
        verbose_name_plural = 'Etiquetas/Tags'
        
    def __str__(self):
        return self.name
    
class Entry(TimeStampedModel):
    """ Modelo para las Entradas """
    # settings.AUTH_USER_MODEL, para indicar el modelo de usuario utilizado por nosotros
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Entry')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    # slug, campo para el posicionamiento SEO, debe llamarse asi
    slug = models.SlugField(editable=False, max_length=300)
    
    objects = EntryManager()
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'        
        
    def __str__(self):
        return self.title
    
    def slug_gen(self):
        """ crear una entrada unica para el slug field """
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        return slugify(slug_unique)
        
    def save(self, *args, **kwargs):       
        """ Al guardar una entrada como portada, la que estaba en potada anteriormente se desactiva """
        if self.portada:
            # .__class__, se utiliza para hacer referencia a la clase del objeto, debe utilizarse aca
            # para poder utilizar los managers
            self.__class__.objects.filter(
                portada=True
            ).exclude(id=self.id).update(portada=False)
            
        # slug_gen, genera una entrada de slug
        self.slug = self.slug_gen()
        return super(Entry,self).save(*args, **kwargs)
    
    # Para el SEO
    def get_absolute_url(self):
        return reverse_lazy("entrada_app:detail", kwargs={"slug": self.slug})
    