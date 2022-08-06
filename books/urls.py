from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, re_path
from .views import index, articles, special_case_2003

urlpatterns = [
    path('', index),
    path('articles/', articles),
    path('articles/2003', special_case_2003),
    path('admin/', admin.site.urls),
]

