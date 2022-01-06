from django.contrib import admin
from django.urls import path
from .views import HelloClass, function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', function),
    path('hello2/', HelloClass.as_view()),
]
