from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def second(request):
    return HttpResponse('<h1><marquee>my second project</marquee></h1>')
def third(request):
    return HttpResponse('hello django!!!')
