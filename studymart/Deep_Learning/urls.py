from django.urls import path
from . import views

urlpatterns = [
    path('dlearning', views.deep_learning),
    path('register/', views.registration),

]
