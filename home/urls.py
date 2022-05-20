from django.contrib import admin
from django.urls import path
from .views import home , Login , Register , hello_world

urlpatterns = [
        path('' , hello_world),
        path('home/' , home  )    ,
        path('Login/' , Login),
        path('Register/' , Register)
       
]
