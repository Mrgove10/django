from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('landing/index.html')
    context = {
        "name": "adrien"
    }  # to passe variables in teh view
    return HttpResponse(template.render(context, request))
