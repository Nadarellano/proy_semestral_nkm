from django.shortcuts import render, redirect
# from requests import request
from .models import Cliente, Arbusto, Macetero,Sustrato,Flor
from .forms import ClienteForm, ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.

def index (request):

    return render(request, 'core/index.html')


def carrito (request):

    return render(request,'core/carrito.html')


def Ceratostigma (request):

    return render(request, 'core/Ceratostigma.html')


def coprosma (request):

    return render(request, 'core/coprosma.html')


def datos_seguimiento (request):

    return render(request, 'core/datos_seguimiento.html')

def Diosma (request):

    return render(request, 'core/Diosma.html')

def girasoles (request):

    return render(request, 'core/girasoles.html')

def leonotis (request):

    return render(request, 'core/leonotis.html')

def liliums (request):

    return render(request, 'core/liliums.html')


def mac_amarillo (request):

    return render(request, 'core/mac_amarillo.html')


def mac_gris(request):

    return render(request, 'core/mac_gris.html')

def mac_negro(request):

    return render(request, 'core/mac_negro.html')

def mac_rojo(request):

    return render(request, 'core/mac_rojo.html')


def nosotros(request):

    return render(request, 'core/nosotros.html')

def pago(request):

    return render(request, 'core/pago.html')

def prod_arbustos(request):

    return render(request, 'core/prod_arbustos.html')

def prod_flores(request):

    return render(request, 'core/prod_flores.html')

def prod_maceteros(request):

    return render(request, 'core/prod_maceteros.html')

def prod_sustratos(request):

    return render(request, 'core/prod_sustratos.html')

# def registrodos(request):

#     return render(request, 'core/registrodos.html')

def rosas(request):

    return render(request, 'core/rosas.html')

def stock(request):

    return render(request, 'core/stock.html')

def terminos_condiciones(request):

    return render(request, 'core/terminos_condiciones.html')

def tierra_biológica(request):

    return render(request, 'core/tierra_biológica.html')

def tierra_compost(request):

    return render(request, 'core/tierra_compost.html')

def tierra_hoja(request):

    return render(request, 'core/tierra_hoja.html')

def tierra_humus(request):

    return render(request, 'core/tierra_humus.html')

def tulipanes(request):

    return render(request, 'core/tulipanes.html')

def ubicacion_compra(request):

    return render(request, 'core/ubicacion_compra.html')

def nandinas(request):

    return render(request, 'core/nandinas.html')

def stenocarpus(request):

    return render(request, 'core/stenocarpus.html')

def veronicas(request):

    return render(request, 'core/veronicas.html')

def datos_cliente(request):

    clientes= Cliente.objects.all()
    

    datos = {
        'clientes' : clientes
        
    }
    return render(request, 'core/datos_cliente.html', datos)

def productos_recomendados(request):

    arbustos= Arbusto.objects.all()
    flores= Flor.objects.all()
    maceteros= Macetero.objects.all()
    sustratos= Sustrato.objects.all()

    datos = {
        'arbustos' :arbustos,
        'flores' : flores,
        'maceteros' : maceteros,
        'sustratos' : sustratos
    }
    return render(request, 'core/productos_recomendados.html', datos)

def prod_maceteros(request):

    maceteros= Macetero.objects.all()

    datos = {
        'maceteros' : maceteros
    }
    return render(request, 'core/prod_maceteros.html', datos)

def prod_sustratos(request):

    sustratos= Sustrato.objects.all()

    datos = {
        'sustratos' : sustratos
    }
    return render(request, 'core/prod_sustratos.html', datos)

def prod_flores(request):

    flores= Flor.objects.all()

    datos = {
        'flores' : flores
    }
    return render(request, 'core/prod_flores.html', datos)

def prod_arbustos(request):

    arbustos= Arbusto.objects.all()

    datos = {
        'arbustos' : arbustos
    }
    return render(request, 'core/prod_arbustos.html', datos)




def registrodos(request):
    datos = {
        'form': ClienteForm()
    }
    
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['message'] = 'Guardado correctamente'
        else:
            datos['message'] = 'Hubo un problema'
    
    
    return render(request, 'core/registrodos.html', datos)

def form_mod_datos (request, id):
    cliente = Cliente.objects.get(rut = id)
    
    datos = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        
        if formulario.is_valid:
            formulario.save()
            datos['message'] = 'Guardado correctamente'
        else:
            datos['message'] = 'Hubo un problema'
    
    
   
    return render(request, 'core/form_mod_datos.html', datos)

def form_del_datos (request, id):
    
    cliente = Cliente.objects.get(rut = id)

    cliente.delete()

    return redirect(to="")


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Vive Verde: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["an.munoze@duocuc.cl"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "core/contact.html",{'form':contact_form})