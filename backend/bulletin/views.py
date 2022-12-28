from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def adminHome(request):
    template = loader.get_template('bulletin/adminHome.html')
    return HttpResponse(template.render({}, request))

