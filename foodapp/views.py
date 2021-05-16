from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Foodapp
from .forms import FoodappForm
# Create your views here.

#READ생성
def begin(request):
    foodapps = Foodapp.objects.all()
    return render(request,'begin.html',{'foodapps':foodapps})

def exact(request, id):
    foodapp = get_object_or_404(Foodapp, pk = id)
    return render(request,'exact.html',{'foodapp':foodapp})

#CREATE생성 ; 글 생성

def fresh(request):
    if request.method == 'POST':  #글을 작성한 후 저장 버튼을 눌렀을 때
        form = FoodappForm(request.POST,request.FILES)
        if form.is_valid():
            new_foodapp = form.save(commit=False)
            new_foodapp.date = timezone.now()
            new_foodapp.save()
            return redirect('begin')
    else:                          #글을 쓰려고 들어갔을 때
        form = FoodappForm()       #글을 입력받기 위한 빈 form을 불러옴
        return render(request,'fresh.html',{'form':form})
'''
#UPDATE생성 ; 글 수정 (revise (edit), reupload (update))
def revise(request, id):
    foodapp = get_object_or_404(Foodapp, pk = id)
    if request.method == 'GET': #수정하려고 들어갔을 때
        form = FoodappForm(instance = foodapp)
        #현재 post(=foodapp)가 포함된 form을 불러옴
        return render(request,'revise.html',{'form': form})
    else:                       #글을 수정하고 수정버튼을 눌렀을 때
        form = FoodappForm(request.POST, request.FILES, instance = foodapp)
        #현재 post(=foodapp)에 가져온 정보를 form에 담음
        if form.is_valid():
            new_foodapp = form.save(commit=False)
            new_foodapp.date = timezone.now()
            new_foodapp.save()
        # return redirect('exact',new_foodapp.id)
        # return redirect('/foodapp/'+str(id))
'''
#UPDATE생성 ; 글 수정 (revise (edit), reupload (update))
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