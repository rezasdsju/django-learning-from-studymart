from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.machine_learning),
    path('rn/', views.random),
    path('knn/', views.K_nearest),
    path('dt/', views.dtree),

]
