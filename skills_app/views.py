from django.shortcuts import render
from django.template import loader  
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.models import User,auth
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UpdatesForm1
from .models import Updates

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
def index_view(request):
    return render(request, "index.html")
def index(request):
   if request.method == "POST":
      form= UpdatesForm1(request.POST)
      if form.is_valid():
         email = form.cleaned_data['email']
         print(email)
         form.save()
 
         send_mail('Subject here','Here is the message.','21051070@kiit.ac.in',[email],fail_silently=False,)
         return redirect("")
         
   else:
        form = UpdatesForm1()
        
   return render(request, "index.html",{'form': form})

class test(CreateView):
    model = Updates
    template_name = 'test.html'
    fields = '__all__'
    success_url = "/test"   

"""
submitted = False
   if request.method == "POST":
      form = UpdatesForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/?submitted=True')
   else:
      form = UpdatesForm
      if 'submitted' in request.GET:
         submitted = Ture
"""
