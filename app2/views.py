from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista2(request):
    html="""
    <h1 style="color:blue" >Hola Mundo app2</h1>

"""
    return HttpResponse(html)