from django.shortcuts import render

# Create your views here.

def tixaction(request):
    render(request, 'tickets.html',{})