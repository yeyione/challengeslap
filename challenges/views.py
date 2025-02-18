from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Este es un mensaje desde el index")
def january(request):
    return HttpResponse("Walk for at least 30 min every day")
def february(request):
    return HttpResponse("Go to the gym every day")
def march(request):
    return HttpResponse("Eate healthy every day")
def april(request):
    return HttpResponse("Sleep 8hr every day")
def may(request):
    return HttpResponse("Be activated")
def june(request):
    return HttpResponse("Stay hydrated")
def july(request):
    return HttpResponse("Dont eat to much sweet")
def august(request):
    return HttpResponse("Practice meditation")
def september(request):
    return HttpResponse("Disconnect from screens before bedtime")
def october(request):
    return HttpResponse("Get enough sunlight")
def november(request):
    return HttpResponse("Wash your hands frequently")
def december(request):
    return HttpResponse("Spend time outdoors")

