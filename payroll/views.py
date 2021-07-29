from django.shortcuts import render,redirect
from payroll.forms import EmployeeForm
from payroll.models import Employee
# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
# def adminpage(request):
#     return render(request, 'admin.html') 
def adminadd(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('mob') and request.POST.get('job') and request.POST.get('doj') and request.POST.get('accno') and request.POST.get('ifsc') and request.POST.get('payscale'):
            saverecord=Employee(fname=request.POST.get('fname'),lname=request.POST.get('lname'),email=request.POST.get('email'),mob=request.POST.get('mob'),job=request.POST.get('job'),doj=request.POST.get('doj'),accno=request.POST.get('accno'),ifsc=request.POST.get('ifsc'),payscale=request.POST.get('payscale'))
            saverecord.save()
            return render(request, 'index.html')
    else:
        return render(request, 'admin.html')        
      
# def register(request):
#     #post data from index.html to database
             


    