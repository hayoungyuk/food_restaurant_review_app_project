from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Foodapp
from .forms import FoodappForm
# Create your views here.

#READ
def begin(request):
    foodapps = Foodapp.objects.all()
    return render(request,'begin.html',{'foodapps':foodapps})

def exact(request, id):
    foodapp = get_object_or_404(Foodapp, pk = id)
    return render(request,'exact.html',{'foodapp':foodapp})

#CREATE
def fresh(request):
    form = FoodappForm()
    return render(request,'fresh.html',{'form':form})

def make(request):
    form = FoodappForm(request.POST,request.FILES)
    if form.is_valid():
        new_foodapp = form.save(commit=False)
        new_foodapp.date = timezone.now()
        new_foodapp.save()
        return redirect('exact',new_foodapp.id)
    return redirect('begin')

#UPDATE
def revise(request,id):
    revise_foodapp = Foodapp.objects.get(id = id)
    return render(request,'revise.html',{'foodapp':revise_foodapp})

def reupload(request,id):
    reupload_foodapp = Foodapp.objects.get(id = id)
    reupload_foodapp.location = request.POST['location']
    reupload_foodapp.eater = request.POST['eater']
    reupload_foodapp.content = request.POST['content']
    reupload_foodapp.date = timezone.now()
    reupload_foodapp.save()
    return redirect('exact',reupload_foodapp.id)

def remove(request, id):
    remove_foodapp = Foodapp.objects.get(id=id)
    remove_foodapp.delete()
    return redirect('begin')