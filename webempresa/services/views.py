from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all() # Traer todos los servicios registrados en el modelo de la App
    return render(request, "services/services.html", {'services': services}) # Realizar el render con los 
                                                                            # servicios importados.
