from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='login'),
    # path('admin_login/',views.admin_login,name='admin_login'),
    path('adminadd/',views.adminadd,name='adminadd'),
    path('admindash/',views.admindash,name='admindash'),
    path('empdash/',views.empdash,name='empdash'),
    path('personal_details/',views.personal_details,name='personal_details'),
    path('statistics/',views.statistics,name='statistics'),
    path('account_details/',views.account_details,name='account_details'),
    path('view_employee/',views.view_employee,name='view_employee'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update)


    ]
