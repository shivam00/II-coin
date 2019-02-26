from django.urls import path
from .views import home,timeline,faq,about




urlpatterns = [
    path('',home,name="home"),
    path('timeline',timeline,name="timeline",),
    path('faq',faq,name="faq",),
    path('about',about,name="about",),
]