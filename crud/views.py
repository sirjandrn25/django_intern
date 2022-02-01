from statistics import median_high
from django.shortcuts import redirect, render,get_object_or_404
from .forms import StudentForm
from .models import Student
from django.views import View
# from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.decorators import method_decorator



class StudentView(View):


    def get(self,request):
        students = Student.objects.all()
        form = StudentForm()
        data = {
            'students':students,
            'form':form
        }
        return render(request,"student/index.html",data)

    @method_decorator(login_required(login_url='/admin/login/'))
    def post(self,request):
        if request.user.is_superuser:
            form = StudentForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,"successfully added new student")
            
            else:
                messages.error(request,"something is wrong")
            
        else:
            messages.info(request,"only superuser can add student")
        return redirect("student")
        
    
    




class StudentDetailView(View):
    def get(self,request,id):
        student = get_object_or_404(Student.objects.all(),pk=id)
    
        form = StudentForm(instance=student)
        data = {
            'student':student,
            'form':form
        }
        return render(request,"student/edit_detail.html",data)
    @method_decorator(login_required(login_url='/admin/login/'))
    def post(self,request,id):
        student = get_object_or_404(Student.objects.all(),pk=id)
        form = StudentForm(data=request.POST,instance=student)
        if request.user.is_superuser:
            if form.is_valid():
                form.save()
                messages.info(request,"successfully updated the messages")
            else:
                messages.error(request,"something is wrong")
        else:
            messages.info(request,"only superuser can modify student")
        return redirect("student")

@login_required(login_url='/admin/login/')
def delete_student(request,id):
    if request.user.is_superuser:
        student = get_object_or_404(Student.objects.all(),pk=id)
        student.delete()
        messages.info(request,"student are deleted successfully")
    else:
        messages.info(request,"only superuser can delete student")
    return redirect("student")

    




    
    
# for api views 
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsSuperuser
from rest_framework.authentication import SessionAuthentication

class StudentApiView(ModelViewSet):
    authentication_classes = [SessionAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsSuperuser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
