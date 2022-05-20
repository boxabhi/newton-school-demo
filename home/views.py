from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Store, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def hello_world(request):
    data = request.data 
    username = data.get('username')
    password = data.get('password')
    Store.objects.create(username = username , password = password)

    return Response({"stats": 200})


def home(request):
    student_objs = Student.objects.all()
    
    page = request.GET.get('page' , 1)
    paginator = Paginator(student_objs , 10)
    try:
        student_objs = paginator.page(page)
    except PageNotAnInteger:
        student_objs = paginator.page(1)
    except EmptyPage:
        student_objs = paginator.page(paginator.num_pages)


    context = {'student_objs' : student_objs} 
    return render(request , 'home.html' , context)



def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username= username).exists():
            return redirect('/Login/')
        
        user_obj = authenticate(username= username , password = password)

        if user_obj:
            login(request , user_obj)
            print('Usern logged in')
            return redirect('/home/')

        print("Wrong password")
        return redirect('/Login/')        



    return render(request , "login.html")


def Register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username= username).exists():
            return redirect('/Register/')


        user_obj = User(first_name = first_name , username=username , password=password)
        user_obj.set_password(password)
        user_obj.save()
        print(f'{first_name} \n {username} \n {password}')
        print("User created")
        return redirect('/Register/')

    return render(request , "register.html")


def Logout(request):
    logout(request)
    return redirect('/')
