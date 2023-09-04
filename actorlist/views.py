from django.http import HttpResponse
from django.template import loader

def   actor(request):
    return HttpResponse("Actor List")
