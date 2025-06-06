from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'name' : 'Pablo',
        'age' : '20',
        'nationality' : 'Polish',
    }
    return render(request, 'index.html', context)
def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info('This username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Your passwords are not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'User does not exist')
            return redirect(request,'login.html')
    return render(request, 'login.html')