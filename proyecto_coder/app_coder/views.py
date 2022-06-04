from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Kiosco
from app_coder.models import Libreria
from app_coder.models import Servicios
from django.template import loader
from app_coder.forms import Alta_formulario
from app_coder.forms import Alta_formulariolibreria
from app_coder.forms import Alta_formularioservicios






def inicio(request):
    return render(request , "plantillas.html")

    

# Create your views here.
def kioscos(request):
    kioscos = Kiosco.objects.all()
    dicc = {"kioscos" : kioscos}
    plantilla = loader.get_template("kioscos.html")
    documento = plantilla.render(dicc)
    
    return HttpResponse( documento )

def alta_kiosco(request, nombre):
    kiosco = Kiosco(nombre=nombre , precio=80)
    kiosco.save()
    texto = f"se guardo en la BD Kiosco: {kiosco.nombre} Precio: {kiosco.precio}"
    return HttpResponse(texto)


def librerias(request):
    librerias = Libreria.objects.all()
    diccionario = {"librerias" : librerias}
    plantilla = loader.get_template("librerias.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse( documento )

def alta_libreria(request, producto):
    libreria = Libreria(producto=producto , precio=100)
    libreria.save()
    texto = f"se guardo en la BD Libreria: {libreria.producto} Precio: {libreria.precio}"
    return HttpResponse(texto)


def servicioss(request):
    servicioss = Servicios.objects.all()
    dicc = {"servicioss" : servicioss}
    plantilla = loader.get_template("servicioss.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )
   
    

def alta_servicios(request, nombre):
    servicios = Servicios(nombre=nombre , precio=40)
    servicios.save()
    texto = f"se guardo en la BD Servicios: {servicios.nombre} Precio: {servicios.precio}"
    return HttpResponse(texto)
    
def librerias(request):
    
    return render( request , "librerias.html" )     

def servicioss(request):
    
    return render(request , "servicioss.html")

def contacto(request):
    
    return render(request, "contacto.html")
    
def alta_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Alta_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
        
        kiosco = Kiosco(nombre=datos['nombre'] , precio=datos['precio'])
        kiosco.save()
        
        return render(request, "formulario.html")
        
        
    return render(request , "formulario.html")    

def buscar_producto(request):
    
    return render( request ,"buscar_producto.html")

def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        kioscos = Kiosco.objects.filter(nombre__icontains = nombre )
        return render( request , "resultado_busqueda.html" , {"kioscos": kioscos})
    
    
    else:
        return HttpResponse("Campo vacio")
    
   
def alta_formulariolibreria(request):
    if request.method == "POST":
        
        mi_formulario = Alta_formulariolibreria( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
        
        libreria = Libreria(producto=datos['producto'] , precio=datos['precio'])
        libreria.save()
        
        return render(request, "formulario_libreria.html")
        
        
    return render(request , "formulario_libreria.html")    


def alta_formularioservicios(request):
    if request.method == "POST":
        
        mi_formulario = Alta_formularioservicios( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
        
        servicios = Servicios(nombre=datos['nombre'] , precio=datos['precio'])
        servicios.save()
        
        return render(request, "formulario_servicios.html")
        
        
    return render(request , "formulario_servicios.html")    
    
    
    
    