from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación") # Este campo nos permite
        # incluir una fecha manual de publicación, aunque por defecto aparece la fecha actual.
    image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen") # Las opciones null=True
        # y blank=True en este campo, hacen que el diligenciamiento de este campo sea opcional.
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor") # Este campo tipo "ForeignKey"
        # importado desde django.contrib.auth.models, y dentro de éste, configurada la opción on_delete=models.CASCADE,
        # le indicará a Django que, al borrar el autor, se borrarán también todas las publicaciones en las que este 
        # usuario sea autor. De ahí lo de "cascada", el modelo User se lleva los modelos relacionados con él.
    categories = models.ManyToManyField(Category, verbose_name="Categorías") # Este campo tipo "ManyToMany", establece
        # una relación de muchos a muchos entre "Post" (publicaciones) y Categories (Categorías), por lo que podremos
        # seleccionar una o más cotegoráias.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación")
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        
    def __str__(self):
        return self.title