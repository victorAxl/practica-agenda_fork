#from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.http import HttpResponse
from django.forms import BaseFormSet, HiddenInput, formset_factory, modelformset_factory
from .forms import ContactoForm, DireccionForm, TelefonoForm
from .models import Contacto, Direccion, Telefono


def inicio(request):
    return redireccion(0, 420)

def home(request, order):
    template = get_template("inicio.html")

    context = {
        "titulo": "Inicio",
        "contactos": Contacto.objects.all().order_by(order)
    }

    return HttpResponse(template.render(context), request)

def contacto_nuevo(request):
    context = {"titulo": "Nuevo contacto",}
    if request.method == "POST":
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()
            Direccion.objects.create(contacto=contacto)
            return redirect('contacto_edicion', pk=contacto.pk)
        else:
            context['form'] = form
    else:
        context['form'] = ContactoForm()
    return render(request, "contacto_nuevo.html", context)

def inicializa_context(pk, titulo, tab):
    contacto = get_object_or_404(Contacto, pk=pk)
    direccion = get_object_or_404(Direccion, contacto__id=pk)
    telefonos = Telefono.objects.filter(contacto__id=pk)
    TelefonoFormSet = modelformset_factory(Telefono, fields=('tipo', 'alias','numero'), can_delete=True)
    context = {
        'telefonoFormSet': TelefonoFormSet(queryset=telefonos), 
        'contacto_form': ContactoForm(instance=contacto), 
        'direccion_form': DireccionForm(instance=direccion), 
        'contacto': contacto, 
        'direccion': direccion, 
        'telefonos': telefonos, 
        'titulo': titulo, 
        'tab': tab, 
        'pk': pk, 
        }

    return context

def contacto_edicion(request, pk):
    context = inicializa_context(pk, 'Editor del contacto', 1)
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST, request.FILES, instance=context['contacto'])
        if contacto_form.is_valid(): 
            contacto = contacto_form.save(commit=False)
            contacto.save()
            return redireccion(request.POST.get('tab', 1), pk)
        else:
            context['contacto_form'] = contacto_form
    return render(request, "contacto_edicion.html", context)

def direccion_edicion(request, pk):
    context = inicializa_context(pk, 'Editor de la dirección', 2)
    if request.method == "POST":
        direccion_form = DireccionForm(request.POST, instance=context['direccion'])
        if direccion_form.is_valid(): 
            direccion = direccion_form.save(commit=False)
            direccion.save()
            return redireccion(request.POST.get('tab', 1), pk)
        else:
            context['direccion_form'] = direccion_form
    return render(request, "contacto_edicion.html", context)

def telefonos_edicion(request, pk):
    context = inicializa_context(pk, 'Editor de telefonos', 3)
    TelefonoFormSet = modelformset_factory(Telefono, fields=('tipo', 'alias','numero'), can_delete=True)
    if request.method == 'POST':
        formset = TelefonoFormSet(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset.new_objects:
                form.contacto_id=pk
            for form in formset:
                if form.instance.tipo and form.instance.alias and form.instance.numero:
                    form.save()
            for form in formset.deleted_objects:
                form.delete()
            return redireccion(request.POST.get('tab', 1), pk)
        else:
            context['telefonoFormSet'] = formset
    return render(request, "contacto_edicion.html", context)

#@deprecated
def telefonos_edicion_(request, pk):
    class BaseArticleFormSet(BaseFormSet):
        deletion_widget = HiddenInput

    TelefonoFormSet = formset_factory(TelefonoForm, formset=BaseArticleFormSet, can_delete=True)
    formset = TelefonoFormSet(initial=Telefono.objects.filter(contacto__id=pk).values())
    context = {
        "titulo": "Editor de contactos",
        'telefonoFormSet': formset,
        'pk':pk,
        'tab': 3,
    }
    if request.method == 'POST':
        formset = TelefonoFormSet(request.POST)
        if formset.is_valid():
            #formset.save(commit=False)
            for form in formset.extra_forms:
                form.save(commit=False)
                form.instance.contacto_id=pk
            for form in formset:
                form.instance.save()
            return redirect('telefonos_edicion', pk=pk)
    return render(request, "contacto_edicion.html", context)

def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redireccion(0, 420)

def redireccion(id, pk):
    id = int(id)
    if id == 0:
        return redirect('home', 'nombre')
    if id == 1:
        return redirect('contacto_edicion', pk=pk)
    if id == 2:
        return redirect('direccion_edicion', pk=pk)
    if id == 3:
        return redirect('telefonos_edicion', pk=pk)
    else:
        return redirect('sfsdfsd', pk=pk)