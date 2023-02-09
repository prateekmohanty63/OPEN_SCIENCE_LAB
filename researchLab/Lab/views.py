from email import message
import re
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import NewuserForm
from django.contrib import messages,auth
from django.contrib.auth import login
from django.contrib.auth.models import User
import json
from django.core.mail import send_mail
from django.http import JsonResponse

# mqtt
from pyPS4Controller.controller import Controller
import os
import struct
import time
import paho.mqtt.client as mqtt

# cloudmpq
import pika,json
from .producer import publish


# redis
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from django.core.cache import caches
import django_rq

# redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)



# Create your views here.


def index(request):
   if request.user.is_authenticated:
      user=request.user
      context={
         'user':user
      }
      return render(request,'index.html',context)
   return render(request,'index.html')

   

def people(request):
    return render(request,'people.html')


def research(request):
   return render(request,'instrumentation.html')


def publication(request):
   return render(request,'publications.html')


def gallery(request):
   return render(request,'gallery.html')

def news(request):
   return render(request,'news.html')

def teaching(request):
   return render(request,'teaching.html')


def contact(request):
   return render(request,'contact.html')

def registration(request):

   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      pwd1=request.POST['pwd1']
      pwd2=request.POST['pwd2']

      print(username,email,pwd1,pwd2)

      if pwd1==pwd2:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('registration')
         
         elif User.objects.filter(email=email).exists():
            messages.info(request,'Email is taken already')
            return redirect('registration')
         else:
            user=User.objects.create_user(
               username=username,
               password=pwd1,
               email=email
            )
            user.save()

            return redirect('index')
      else:
         messages.info(request,"Password not matching")
         return redirect("registration")


  

   return render(request,'registration.html')

def login(request):
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']

      user=auth.authenticate(request,username=username,password=password)

      if user is not None:
         auth.login(request,user)
         messages.success(request,"signed in successfully")
         return redirect('index')
      else:
         messages.info(request,'login failed')
         return redirect('login')
   return render(request,'login.html')

def logout(request):
   user=request.user
   context={
      'USER':user
   }
   auth.logout(request)
   messages.success(request, "Signed out successfully", context)
   return redirect('index')


def add_queue(argv):
   a=""
   for arg in argv:
      a=a+arg
   return a




def expirement1(request):

   if request.method=="POST":
      
        # Checking weather the user is signed in or not
      if not request.user.is_authenticated:
       messages.error(request, "Please sign in ")
       return redirect('index')
      
      user = User.objects.all().filter(username=request.user.username).get()

      q=[]

      

   

      ninputs=request.POST['ninputs']
      
      if ninputs!='':
         n=int(ninputs)
      else:
         n=2
   

      slot=request.POST['slot']
    

      if slot=='':
         messages.info(request,'Please select the slot of test tube')
         return redirect('expirement')
      
      # conveting the request.POST into json format
      s1 = json.dumps(request.POST)
      item = json.loads(s1)
      # print(item)

      count=0
      
      
      for i in range(n-1):
         ingrident=request.POST['ingredient'+str(i+1)]
         #print(ingrident)
         q.append(ingrident)

         amount=request.POST['amt'+str(i+1)]
         #print(amount)
         q.append(amount)
      
      reactionEq=request.POST['expText']
      print(reactionEq)



      q.append(slot)
      q.append(reactionEq)

       # setting up redis queue
      if not request.session.session_key:
        request.session.save()
      session_id = request.session.session_key

      redis_cache=caches['default']

      queue=django_rq.get_queue('default')

      queue.enqueue(add_queue,q)

      print(queue.get_job_ids(0))

      jobid=queue.get_job_ids(0)[-1]

      print(jobid)
      
      
      reactants=""

      for i in range(0,len(q),2):
         reactants=reactants+q[i]+" "
      
      print(reactants)

     
      

     
      messages.info(request,'Your expirement was been added to the queue , we will reach back to you once the results are ready')

      # email sending
      # userSubject = "Reference for your expirement "
      # userBody = ("Hi "+user.username+
      #             "\n\nYour expirement has been successfully added to the queue"+
      #             "\n\n Expirement-id: "+jobid+
      #             "\n\n slot choosen: "+slot+
      #             "\n\n reactants given: "+reactants+
      #             "\n\n we will let you know once the results are ready"
      #           )
      # useremail = send_mail (
      #           userSubject,
      #           userBody,
      #           "prateekmohanty63@gmail.com",
      #           ['prateekmohanty63@gmail.com'],
      #           fail_silently=False
      #   )



      return redirect('index')


   return render(request,'testExpirement-1.html')


def peak(request):

   if request.method=="GET":

      queue=django_rq.get_queue('default')
      

      if queue.is_empty():
         return HttpResponse("Queue is empty !!!")


      

   # print(queue.get_job_ids(0))
      jobId=queue.get_job_ids()[0]
      #print(jobId)
     
      # print(queue.get_jobs()[0].args[0])

      q=queue.get_jobs()[0].args[0]

      # publishing the ingridents
      payload=""
      for i in range(0,len(q)-1,2):

       payload=payload+queue.get_jobs()[0].args[0][i]+" "
      
      payload=payload+" ,"

      # publishing the quantities


      for i in range(1,len(q),2):
         payload=payload+queue.get_jobs()[0].args[0][i]+" "

      payload=payload+" ,"


      payload=payload+queue.get_jobs()[0].args[0][-1]

      print(payload)  
      
      res={'expirement':payload}
      
  
      publish('peak_value',payload)

      return JsonResponse(res)
   
  
   


def dequeue(request):

# setting up redis queue
   if request.method=="GET":

      # if not request.session.session_key:

      #    request.session.save()
      #    session_id = request.session.session_key

      redis_cache=caches['default']

      queue=django_rq.get_queue('default')

      if queue.is_empty():
         return HttpResponse('Queue is empty . No expirements to Dequeue')
     

    
      queue.pop_job_id()
   


      return HttpResponse('Expirement dequeued')
   # return HttpResponse('Expirement dequeued')



def work(request):
   return render(request,'works.html')

def useLab(request):
   return render(request,'use.html')


def demo(request):
   if request.method=="POST":
      client=mqtt.Client()
      client.connect("broker.mqttdashboard.com", 1883, 60)
      res=request.POST['res']
      #print(res)
      msg=res
      print(msg)
      client.publish('charan/1', payload=msg, qos=0, retain=False)
      return HttpResponse("Value given")
   return render(request,'demo.html')




# redined pages
def work1(request):
   return render(request,'works-1.html')

def use1(request):
   return render(request,'use-1.html')

def research1(request):
   return render(request,'instrumentation-1.html')


   