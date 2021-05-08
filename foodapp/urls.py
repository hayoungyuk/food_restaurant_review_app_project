from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',exact,name='exact'),
    path('fresh/',fresh,name="fresh"),
    path('make/',make,name="make"),
    path('revise/<str:id>',revise,name="revise"),
    path('reupload/<str:id>',reupload,name="reupload"),
    path('remove/<str:id>',remove,name = "remove"),
]