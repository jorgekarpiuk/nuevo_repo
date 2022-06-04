from django import forms

class Alta_formulario(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    precio= forms.IntegerField()

class Alta_formulariolibreria(forms.Form):
    
    producto= forms.CharField(max_length=40)
    precio= forms.IntegerField()

class Alta_formularioservicios(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    precio= forms.IntegerField()
        
    
      