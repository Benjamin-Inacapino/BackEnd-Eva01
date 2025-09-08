from django.shortcuts import render
from . import models


def home(request):
    productos_top = models.Producto.objects.order_by('-precio')[:3]
    return render(request,"core/home.html", {"actual_endpoint": "inicio", "productos": productos_top, "comentarios": models.Comentario.objects.all()})

def faq(request):
    return render(request,"core/faq.html", {"actual_endpoint": "faq"})

def quienes_somos(request):
    return render(request, "core/quienes_somos.html", {"actual_endpoint": "quienes-somos"})

def productos(request):
    return render(request, "core/productos.html", {"actual_endpoint": "productos", "productos": models.Producto.objects.all()})
