from django.contrib import admin
from django.urls import path
from .views import home , Login , Register

urlpatterns = [
        path('home/' , home  )    ,
        path('Login/' , Login),
        path('Register/' , Register)
       
]
