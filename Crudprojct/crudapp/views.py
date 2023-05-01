from django.shortcuts import render,redirect

# Create your views here.
from crudapp.models import StudentModel
from crudapp.forms import StudentInfoForm

def registration(request):
    if request.method =="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        address=request.POST.get("address")
        StudentModel.objects.create(name=name,phone=phone,email=email,address=address)
        return render(request,'index.html')
    return render(request,'index.html')


def show(request):
    info=StudentModel.objects.all()
    
    return render(request,'show.html',{'key':info})


def deletedata(request,id):
    stud_id=StudentModel.objects.filter(id=id).first()
    stud_id.delete()
    return redirect('show')

def editData(request,id):
    studobj=StudentModel.objects.filter(id=id).first()
    if request.method=="POST":
        
        
        studobj.name=request.POST.get("name")
        studobj.phone=request.POST.get("phone")
        studobj.email=request.POST.get("email")
        studobj.address=request.POST.get("address")
        studobj.save()
    return render(request,'edit.html',{'data':studobj})