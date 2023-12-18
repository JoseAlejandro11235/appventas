from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),


    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),


    #CRUD AREAS

    path('dashboard-area', views.dashboard_area, name="dashboard-area"),
    path('create-area', views.create_area, name="create-area"),
    path('update-area/<int:pk>', views.update_area, name='update-area'),
    path('area/<int:pk>', views.singular_area, name="area"),
    path('delete-area/<int:pk>', views.delete_area, name="delete-area"),




    #CRUD RECORDS

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),
    
    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

]







