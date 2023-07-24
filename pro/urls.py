from django.urls import path
import pro.views

urlpatterns = [
    path('',pro.views.home,name = 'home'),
]