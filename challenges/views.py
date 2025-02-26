from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenge = {
    "january" : "Walk for at least 30 min every day",
    "february" : "Go to the gym every day",
    "march" : "Eat healthy every day",
    "april" : "Sleep 8 hours every day",
    "may" : "Be active",
    "june" : "Stay hydrated",
    "july" : "Dont eat to much sweet",
    "august" : "Practice meditation",
    "september" : "Disconnect from electronics before bedtime",
    "october" : "Get enough sunlight",
    "november" : "Wash your hands frequently",
    "december" : "Spend time outside"
}

def index(request):
    return HttpResponse("Este es un mensaje desde el index")


def  monthly_challenges(request, month):
    try:
        challenge_text = challenge[month]
        return render (request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1> Este mes no existe</h1>")
def monthly_challenges_number(request, month):
    months = list(challenge.keys())
    
    if month > len(months) or month < 1:
        return HttpResponseNotFound("<h1> Este mes no existe</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

   

    