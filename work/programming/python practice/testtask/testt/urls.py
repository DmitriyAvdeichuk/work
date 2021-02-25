from django.urls import path
from .views import toys

urlpatterns = [
    path('toys/', toys),
]
