from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',exact,name='exact'),
    path('fresh/',fresh,name="fresh"),
    path('revise/<str:id>',revise,name="revise"),
    path('remove/<str:id>',remove,name = "remove"),
]