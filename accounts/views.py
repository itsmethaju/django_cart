from django.contrib import messages
from django.shortcuts import render, redirect


from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username =username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user not valid')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already created")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"user already created")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name, )
                user.save();
                print('user created')
        else:
            
            return render(request,"index.html")
            
    else:

        return render(request, 'registeration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')