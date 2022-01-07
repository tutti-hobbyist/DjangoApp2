from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HelloClass, function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', function),
    path('hello2/', HelloClass.as_view()),
    path('helloapp/', include('helloApp.urls')),
]
