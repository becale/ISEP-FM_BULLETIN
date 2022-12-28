from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages



def index(request):
   template = loader.get_template('account/login.html')
   return HttpResponse(template.render({}, request))  

def login(request):
   if request.method == 'POST':
      username = request.POST["username"]
      password = request.POST["password"]

      user = authenticate(username=username, password=password)

      if user is not None:
         login(request, user)
         return render(request, "")
         # redirect to a success page
      else:
         messages.add_message(request, messages.INFO, "Identifiant ou mot de passe incorect")
         
   #template = loader.get_template('account/login.html')
   #return HttpResponse(template.render({}, request)) 
   return HttpResponse(render("<p>Hello</p>")) 


def signOut(request):
    pass
    