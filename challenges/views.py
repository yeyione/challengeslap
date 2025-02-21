from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

#def monthly_challenges(request, month):
    #challenge_text = challenge.get(month)
    #if challenge_text:
    #    return HttpResponse(challenge_text)
   # else:
  #      return HttpResponseNotFound("Este mes no existe")
#def monthly_challenges_numer(request, month):
#    month_name = dicc.get(month)
 #   if month_name:
  #      return monthly_challenges(request, month_name)
   # else:
    #    return HttpResponseNotFound("Este mes no existe")##

def  monthly_challenges(request, month):
    #try:
        challenge_text = challenge[month]
        return render (request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    #except:
        return HttpResponseNotFound("<h1> Este mes no existe</h1>")