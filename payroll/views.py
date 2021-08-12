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
def empdash(request):
    return render(request, 'Dashboard Employee/empdash.html')  
def personal_details(request):
    return render(request, 'Dashboard Employee/personal_details.html')     
def statistics(request):
    return render(request, 'Dashboard Employee/statistics.html') 
def account_details(request):
    return render(request, 'Dashboard Employee/account_details.html')
def payscale(request):
    return render(request, 'Dashboard Admin/payscale.html')
# def admin_login(request):
#     username1='admin'
#     password1='admin'
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         if username1==username and password1==password:
#             return redirect('admindash')
#         else:
#             return render( request, 'login.html')    
        

#     else:
#         return render(request, 'login.html')

            
def user_login(request):
    username2='john'
    password2='john'
    username1='admin'
    password1='admin'
    #authentication
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username2==username and password2==password:
            return redirect('empdash')
        elif username1==username and password1==password:
            return redirect('admindash')    
        else:
            return render( request, 'login.html')  
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
            return redirect('admindash')
    else:
        return render(request, 'admin.html')        
      
# def register(request):
#     #post data from index.html to database
             


def view_employee(request):
    emps=Employee.objects.all()
    return render(request, 'view_employee.html',{'emps':emps})

def delete(request,id):
    emps=Employee.objects.get(id=id)
    emps.delete()
    return redirect('/view_employee')
def edit(request,id):
    emps=Employee.objects.get(id=id)
    
    return render(request,'edit_employee.html',{'emps':emps})    
def update(request,id):
    emps=Employee.objects.get(id=id)
    
    form=EmployeeForm(request.POST,instance=emps)
    if form.is_valid:
        form.save()
        return redirect('/view_employee')
