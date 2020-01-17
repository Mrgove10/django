from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Little
# Create your views here.


def index(request):
    template = loader.get_template('landing/index.html')
    context = {
        "name": "adrien"
    }  # to passe variables in teh view
    return HttpResponse(template.render(context, request))


def littlepage(request, id):
    try:
        littleVar = Little.objects.get(pk=id)
    except Little.DoesNotExist:
        raise Http404
    # the equivant of thsi try catch is :
    #littleVar = get_list_or_404(Little, pk=id)[0]
    template = loader.get_template('landing/littlepage.html')
    context = {
        "little": littleVar
    }
    return HttpResponse(template.render(context, request))
