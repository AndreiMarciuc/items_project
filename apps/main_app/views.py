from django.shortcuts import render,redirect
from django.contrib import messages
from ..login_app.models import User
from models import Item
import datetime
# from models import 

# Create your views here.
def home(request):
    context = {
        'myself':User.objects.get(id=request.session['id']),
        'cur_user': User.objects.get(id=request.session['id']),
        'items':Item.objects.all()
    }
    return render(request,'main_app/index.html',context)

def new(request):
    return render(request,'main_app/new.html')

def create(request):
    Item.objects.create( brand = request.POST['brand'], date_add = request.POST['date_add'])
    
    return redirect('/home')

def addItem(request,id):
    item=Item.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    user.items.add(item)
    return redirect('/home')

def removeItem(request,id):
    item=Item.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    user.items.remove(item)
    return redirect('/home')

def show(request,id):
    context={
        'item':Item.objects.get(id=id),
        'cur_user': User.objects.get(id=request.session['id']),
        'items':Item.objects.all()
    }
    return render(request,'main_app/show.html',context)