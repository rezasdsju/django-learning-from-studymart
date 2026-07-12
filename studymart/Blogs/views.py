from django.shortcuts import render
from django.http import HttpResponse
from . forms import TeachersRegistration

# Create your views here.


def blog1(request):
    return render(request, 'blogs/blogs.html')


def showformsdata(request):
    fm = TeachersRegistration()
    fm.order_fields(field_order=['email', 'last_name', 'first_name'])
    return render(request, 'blogs/forms.html', {'form': fm})
