from django.urls import path
from .views import helloappview

urlpatterns = [
    path('helloapp/', helloappview)
]
