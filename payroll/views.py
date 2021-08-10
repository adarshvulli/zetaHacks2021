from django.shortcuts import render,redirect
from payroll.forms import EmployeeForm
from payroll.models import Employee, superadmin
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')
def admindash(request):
    return render(request, 'Dashboard Admin/admindash.html')
def admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        admin=authenticate(username=username,password=password)
        if admin is not None:
            login(request,admin)
            return redirect('admindash')
        else:
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')

            
def user_login(request):
    username='john'
    password='john'
    #authentication
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username==username and password==password:
            return redirect('/')
        

    else:
        return render(request, 'login.html')
def logout(request):
    logout(request)
    return render(request, 'login.html')

# def adminpage(request):
#     return render(request, 'admin.html') 
def adminadd(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('username') and request.POST.get('password') and request.POST.get('mob') and request.POST.get('job') and request.POST.get('doj') and request.POST.get('accno') and request.POST.get('ifsc') and request.POST.get('payscale'):
            saverecord=Employee(fname=request.POST.get('fname'),lname=request.POST.get('lname'),email=request.POST.get('email'),username=request.POST.get('username'),password=request.POST.get('password'),mob=request.POST.get('mob'),job=request.POST.get('job'),doj=request.POST.get('doj'),accno=request.POST.get('accno'),ifsc=request.POST.get('ifsc'),payscale=request.POST.get('payscale'))
            saverecord.save()
            return render(request, 'index.html')
    else:
        return render(request, 'admin.html')        
      
# def register(request):
#     #post data from index.html to database
             


    