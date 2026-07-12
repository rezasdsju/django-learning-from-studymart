from django.http import HttpResponse
from django.shortcuts import render
from About_Us.models import Teachers

# Create your views here.
def about_us(request):
    return render(request, 'about/about.html')

def teachers_info(request):
    teach = Teachers.objects.all()
    return render(request, 'about/t.html', {'thr': teach})
