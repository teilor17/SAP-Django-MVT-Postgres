from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.

def ver_detalle(request,id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

def nuevaPersona(request):
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'forma_persona': forma_persona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST, instance=persona)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'forma_persona': forma_persona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')