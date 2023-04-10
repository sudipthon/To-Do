from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
        path('register/',views.Register,name='register'),
        path('login/',views.Log,name='login'),
        path('logout/',views.LogOut,name='logout'),
        # path('add/',views.Add,name='add'),
        path('delete/<str:pk>/',views.Delete,name='delete'),
        path('edit/<str:pk>/',views.Edit,name='edit'),
        path('date/',views.ByDate,name='date'),

]