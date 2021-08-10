from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='login'),
    # path('admin_login',views.admin_login,name='admin_login'),
    path('adminadd/',views.adminadd,name='adminadd'),
    path('admindash/',views.admindash,name='admindash')


    ]
