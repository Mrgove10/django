from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Little
# Create your views here.


def index(request):
    template = loader.get_template('landing/index.html')
    context = {
        "name": "adrien"
    }  # to passe variables in teh view
    return HttpResponse(template.render(context, request))


def littlepage(request,id):
    littleVar = Little.objects.get(pk=id)
    if littleVar != None:
        template = loader.get_template('landing/littlepage.html')
        context = {
            "little": littleVar
        }
        return HttpResponse(template.render(context, request))
    
