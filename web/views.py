from django.shortcuts import render

def index(request):
    return render(request,'web/index.html')

def login(request):
    return render(request,'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password)
    else:
        return render(request,'web/register.html')