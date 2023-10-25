from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    p1=persona("pedro", "rueda")

    #nombre="pedro"
    #apellido="rueda"

    values=["forms", "values", "etc"]

    ahora=datetime.datetime.now()

    #doc_externo=open("/home/pedro/Desktop/Django Project/proyecto1/templates/plantilla.html")
    #plt=Template(doc_externo)
    #doc_externo.close()

    #doc_externo=get_template('plantilla.html')

    #ctx=Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "actual": ahora, "values": values})

    #documento=doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "actual": ahora, "values": values})

    return render(request, 'plantilla.html', {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "actual": ahora, "values": values})

def fecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse(fecha_actual)

def edad(request, agno, edad):
    periodo=agno-2023
    edadF=edad+periodo
    return HttpResponse(edadF)