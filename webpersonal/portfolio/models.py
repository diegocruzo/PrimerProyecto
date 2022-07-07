from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200) # Campo de carácteres definido en los modelos de Django, es una cadena de caracteres en la base de datos
    description = models.TextField() # Campo de texto más grande
    image = models.ImageField() # Campo de imágen en la base de datos
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se añadirá automáticamente cuando se cree la primera vez.
    updated = models.DateTimeField(auto_now=True)  # Fecha de actualización o fecha de modificación, la diferencia respecto al anterior
                                                    # es que este se ejecuta cada vez que se actualiza una instancia