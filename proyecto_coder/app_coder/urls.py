from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio , name= "inicio"),
    path("kioscos" , views.kioscos, name = "kioscos"),
    path("alta_kiosco/<nombre>" , views.alta_kiosco),
    path("librerias" , views.librerias ,name = "librerias"),
    path("alta_libreria/<producto>" , views.alta_libreria),
    path("servicioss" , views.servicioss, name = "servicioss"),
    path("alta_servicios/<nombre>" , views.alta_servicios),
    path("contacto" , views.contacto),
    path("alta_formulario" , views.alta_formulario),
    path("buscar_producto" , views.buscar_producto),
    path("buscar" , views.buscar),
    path("alta_formulariolibreria" , views.alta_formulariolibreria),
    path("alta_formularioservicios" , views.alta_formularioservicios),
    
    
    
    
    

]