from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from App_control.models import Articulos, delivery, Cliente
from App_control.forms import ArticuloFormulario


class clienteListView(ListView):
    model = Cliente
    template_name = 'App_control/lista_cliente.html'


class clienteCreateView(CreateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'email')
    success_url = reverse_lazy('lista_cliente')


class clienteDetailView(DetailView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')


class clienteUpdateView(UpdateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'email')
    success_url = reverse_lazy('lista_cliente')



class clienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')




def listar_articulos(request):
    contexto = {
        "articulos": Articulos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='App_control/lista_articulos.html',
        context=contexto,
    )
    return http_response

def crear_articulos(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            marca = data["marca"]
            precio = data["precio"]
            # creo un curso en memoria RAM
            articulos = Articulos(nombre=nombre, marca=marca ,precio=precio)
            # Lo guardan en la Base de datos
            articulos.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_articulos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario()
        http_response = render(
        request=request,
        template_name='App_control/formulario_articulos.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_articulos(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        articulos = Articulos.objects.filter(marca__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "articulos": articulos,
            "busqueda": busqueda, 
        }
        http_response = render(
            request=request,
            template_name='App_control/lista_articulos.html',
            context=contexto,
        )
        return http_response
   
def eliminar_articulos(request, id):
    # obtienes el curso de la base de datos
    articulos = Articulos.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        articulos.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_articulos')
        return redirect(url_exitosa)
    
    
def editar_articulos(request, id):
    articulos = Articulos.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulos.nombre = data['nombre']
            articulos.marca= data['marca']
            articulos.precio= data['precio']
            articulos.save()

            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': articulos.nombre,
            'marca': articulos.marca,
            'precio': articulos.precio,
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name='App_control/formulario_articulos.html',
        context={'formulario': formulario},
    )

class deliveryListView(ListView):
    model = delivery
    template_name = 'App_control/lista_delivery.html'


class deliveryCreateView(CreateView):
    model = delivery
    fields = ('nombre', 'ubicacion', 'habilitado')
    success_url = reverse_lazy('lista_delivery')


class deliveryDetailView(DetailView):
    model = delivery
    success_url = reverse_lazy('lista_delivery')


class deliveryUpdateView(UpdateView):
    model = delivery
    fields = ('nombre', 'ubicacion', 'habilitado')
    success_url = reverse_lazy('lista_delivery')



class deliveryDeleteView(DeleteView):
    model = delivery
    success_url = reverse_lazy('lista_delivery')




