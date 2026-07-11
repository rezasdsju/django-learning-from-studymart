from django.urls import path
from . import views

urlpatterns = [
    path('data_a', views.data_analysis),

]
