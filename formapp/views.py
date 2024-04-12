from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request,'home.html')
    else:
        Student(
            sname=request.POST.get('sname'),
            lname=request.POST.get('lname'),
            age=request.POST.get('age'),
            mob=request.POST.get('mobile')
        ).save()
        return render(request,'result.html')    