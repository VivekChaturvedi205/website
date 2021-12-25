from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from myapp.models import GK_Knowledge,client1
from django.contrib import auth
from django.core.mail import send_mail


def quizresult(request):
    if request.method=='POST':
        print(request.POST)
        questions=GK_Knowledge.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.Group))
            print(q.answer)
            print()
            if q.answer==request.POST.get(q.Group):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent=score/(total*10)*100
        context={
            'score':score,
            'time':request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, 'myapp/Quiz_result.html',context)
    else:
        questions=GK_Knowledge.objects.all()
        context={
            'question':questions
        }
        return render(request, 'myapp/Gk_knowledge.html',context)

def show_list(request):
    clients1=client1.objects.all()
    data={'clients1':clients1}
    res=render(request, 'myapp/client_list.html',data)
    return res

def saveclient(request):
    if request.method=='POST':
        data=request.POST
        cl=client1()
        cl.First=data['First']
        cl.Last=data['Last']
        cl.Phone=data['Phone']
        cl.Query=data['Query']
        cl.save()
    s="http://localhost:8000/client_list/"
    return redirect(s)

def home(request):
    res=render(request, 'myapp/Index.html')
    return HttpResponse(res)

def sign_up(request):
    res=render(request, 'myapp/Sign_up.html')
    return HttpResponse(res)

def Process(request):
    if request.method=='POST':
        if request.POST['Password'] == request.POST['AgainPassword']:
            try:
                user=User.objects.get(username=request.POST['UserName'])
                return render(request,'myapp/Sign_up.html', {'error':"Username Already exist"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['UserName'],password=request.POST['Password'])
                return redirect("http://localhost:8000/login/")
        else:
            return render(request,'myapp/Sign_up.html', {'error':"Password Don't Match"})
    else:
        return render(request,'myapp/Sign_up.html')

def login(request):
    res=render(request, 'myapp/login.html')
    return HttpResponse(res)

def login_process(request):
    if request.method=='POST':
        #check User is exist
        UserName=request.POST['UserName']
        Password=request.POST['Password']
        user=auth.authenticate(username=UserName, password=Password)
        if user is not None:
            auth.login(request, user)
            request.session['UserName']=UserName
            return redirect("http://localhost:8000/result/")
        else:
            return render(request, 'myapp/login.html',{'error':"Invalid login Credentials!!"})
    else:
            res=render(request, 'myapp/login.html')

def result(request):
    if 'UserName' not in request.session:
        return redirect("http://localhost:8000/login/")
    res=render(request, 'myapp/sucess.html')
    return HttpResponse(res)

def logout(request):
    auth.logout(request)
    return redirect("http://localhost:8000/")

def Quiz1(request):
    if 'UserName' not in request.session:
        return redirect("http://localhost:8000/login/")
    GK_Knowledges=GK_Knowledge.objects.all()
    data={'GK_Knowledges':GK_Knowledges}
    res=render(request, 'myapp/Gk_knowledge.html',data)
    return res

def home1(request):
    # send_mail(
    # 'Testing mail',
    # 'hello chaubey ji',
    # 'modernpkweb04@gmail.com',
    # ['vk126789@gmail.com'],
    # fail_silently=False,)
    res=render(request, 'myapp/Index1.html')
    return HttpResponse(res)

