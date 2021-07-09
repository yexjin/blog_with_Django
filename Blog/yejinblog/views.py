from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import Project
from django.utils import timezone
from .models import Project_ing
from .models import Study
from .forms import ProjectingForm

def main(request):
    projects = Project.objects.all()
    projects_ing = Project_ing.objects.all()
    studies = Study.objects.all()
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

def new(request):
    return render(request, 'create_project.html')


def detail(request, id):
    project = get_object_or_404(Project,pk = id)
    return render(request, 'detail.html', {'project':project})

def create(request):
    # 블로그 객체 만들기
    new_project = Project()

    # new.html에서 정보 가져와서(request.POST), 할당하기
    new_project.title = request.POST['title']
    new_project.project_name= request.POST['project_name']
    new_project.body = request.POST['body']
    new_project.img = request.FILES['image']
    new_project.pub_date = timezone.now()     # 현재 시각을 나타내줌.
    new_project.save() # 이거 해주깅!

    #여기서는 render을 사용하지 않는다. 원래 페이지로 돌아가야함!
    #새로만든 new_blog의 detail로 이동! (새로운 객체의 아이디를 보내줘야함. )
    return redirect('detail', new_project.id)

def edit(request, id):
    edit_projects = Project.objects.get(id=id)
    return render(request, 'edit_project.html', {'project':edit_projects})

def update(request, id):
    update_project = Project.objects.get(id = id)
    update_project.title = request.POST['title']
    update_project.project_name = request.POST['project_name']
    update_project.body = request.POST['body']
    update_project.img = request.FILES['image']
    update_project.pub_date = timezone.now()    
    update_project.save() 
    return redirect('detail', update_project.id)

def delete(request, id):
    delete_project = Project.objects.get(id=id)
    delete_project.delete()
    return redirect('project')

######### 진행중인 프로젝트
def new_projecting(request):
    project_form = ProjectingForm()
    return render(request, 'create_projecting.html',{'project_form':project_form})

def detail_projecting(request, id):
    project_ing = get_object_or_404(Project,pk = id)
    return render(request, 'detail_projecting.html', {'project_ing':project_ing})


def create_projecting(request):
    project_form = ProjectingForm(request.POST)
    if project_form.is_valid():   #유효성 검사
        new_projecting = project_form.save(commit=False) #임시 저장
        new_projecting.pub_date_ing = timezone.now()
        new_projecting.save()
        return redirect('detail_projecting', new_projecting.id)
    return redirect('project')

def delete_projecting(request, id):
    delete_projecting = Project_ing.objects.get(id=id)
    delete_projecting.delete()
    return redirect('project')

#### Study
def study(request):
    studies = Study.objects.all()
    return render(request, 'study.html', {'studies':studies})