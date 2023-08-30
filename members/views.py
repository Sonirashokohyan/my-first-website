from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member
from .models import contact_model

def home(request):
  properties=Member.objects.all().order_by('id')
  Data={
    'properties': properties
  }
  return render(request,"index.html",Data)

def property(request,detid):
  property_details=Member.objects.get(id=detid)
  data={
    'property_details':property_details
  }
  return render(request,"property.html",data)

def contact(request):
  return render(request,"contact.html")
def men(request):
  return render(request,"men.html")
def women(request):
  return render(request,"women.html")
def savecontact(request):
  if request.method=='POST':
    fullname=request.POST.get('fullname')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    contact_= contact_model(full_name=fullname,email=email,subject=subject,message=message)
    contact_.save()
  return render(request,'contact.html')
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())