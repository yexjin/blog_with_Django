from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import Project
from django.utils import timezone
from .models import Project_ing
from .models import Study
from .forms import ProjectingForm

def main(request):
    projects = Project.objects.all().order_by('-id')
    projects_ing = Project_ing.objects.all().order_by('-id')
    studies = Study.objects.all().order_by('-id')
    if request.method == "POST": 
        text = request.POST.get('text_input') # post method를 사용해서 text_input을 가져오자(Get)
        word_list = text.split(' ')
        word_num = len(word_list)
        return render(request,"main.html", {"word_num":word_num}, {"text":text})
    return render(request,"main.html", {'projects':projects, 'projects_ing':projects_ing, 'studies':studies})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        username_DB = "yexjin"
        password_DB = "1234"
        if username == username_DB and password == password_DB:
            return redirect('main')
        else:
            error_message= "틀렸어요"
            return render(request, 'login.html', {"error_message" : error_message})
    return render(request, "login.html")

def guest(request):
    userName = request.GET['name']
    # guest.html에서 이름 가져오기
    return render(request,"guest.html", {'userName':userName})
    # hello.html로 userName이라는 이름을 가진 값이 들어가게 된다.



########## 진행했던 프로젝트
def project(request):
    # Project 테이블에 있는 객체들을 싹 다 가져와서 projects에 저장
    projects = Project.objects.all()
    projects_ing = Project_ing.objects.all()
    return render(request,'project.html', {'projects':projects, 'projects_ing':projects_ing})

def detail(request, id):
    project = get_object_or_404(Project,pk = id)
    return render(request, 'detail.html', {'project':project})

######### 진행중인 프로젝트
def detail_projecting(request, id):
    project_ing = get_object_or_404(Project,pk = id)
    return render(request, 'detail_projecting.html', {'project_ing':project_ing})

#### Study
def study(request):
    studies = Study.objects.all()
    return render(request, 'study.html', {'studies':studies})