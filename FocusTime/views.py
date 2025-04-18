from django.shortcuts import render, redirect
from .models import Materia
from .models import Meta

# Create your views here.

def index (request):
    materias = Materia.objects.all()
    return render(request, "index.html", {"materias": materias})


def cadastro (request):
    if request.method == 'POST':
        nome_materia = request.POST.get('nome-materia')
        horas1 = request.POST.get('horas')
        horas2 = request.POST.get('horas2')
        horas = str(horas1) + str(horas2) if horas1 and horas2 else '00'

        minutos1 = request.POST.get('minutos')
        minutos2= request.POST.get('minutos2')
        minutos = str(minutos1) + str(minutos2) if minutos1 and minutos2 else '00'

        segundos1 = request.POST.get('segundos')
        segundos2 = request.POST.get('segundos2')
        segundos = str(segundos1) + str(segundos2) if segundos1 and segundos2 else '00'

        nome_meta = request.POST.get('nome-meta')
        horas_meta1 = request.POST.get('horas-meta')
        horas_meta2 = request.POST.get('horas-meta2')
        horas_meta = str(horas_meta1) + str(horas_meta2) if horas_meta1 and horas_meta2 else '00'

        minutos_meta1 = request.POST.get('minutos-meta')
        minutos_meta2 = request.POST.get('minutos-meta2')
        minutos_meta = str(minutos_meta1) + str(minutos_meta2) if minutos_meta1 and minutos_meta2 else '00'

        segundos_meta1 = request.POST.get('segundos-meta')
        segundos_meta2 = request.POST.get('segundos-meta2')
        segundos_meta = str(segundos_meta1) + str(segundos_meta2) if segundos_meta1 and segundos_meta2 else '00'

        if nome_materia and horas and minutos and segundos and nome_meta and horas_meta and minutos_meta and segundos_meta:
            materia = Materia(
                nome_materia=nome_materia,
                horas=horas,
                minutos=minutos,
                segundos=segundos,
            )
            meta = Meta(
                nome_metas=nome_meta,
                horas_meta=horas_meta,
                minutos_meta=minutos_meta,
                segundos_meta=segundos_meta,
            )
            meta.save()
            materia.save()
            return redirect('index')
        else:

            return render(request, "cadastro.html")
        
    
    return render (request ,"cadastro.html")


def cronometro (request):
    materias = Materia.objects.all()
    metas = Meta.objects.all()
    contexto = {
        "materias": materias,
        "metas": metas
    }
    return render (request,"cronometro.html" , contexto)

def tela_cadastro (request):
    return render (request , "tela_cadastro.html")