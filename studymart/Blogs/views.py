from django.shortcuts import render
from django.http import HttpResponse
from . forms import TeachersRegistration

# Create your views here.


def blog1(request):
    return render(request, 'blogs/blogs.html')


def showformsdata(request):
    if request.method == 'POST':
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
            
            #print(fm)
            #print('This is post statement')
        
        #fm.order_fields(field_order=['email', 'last_name', 'first_name'])
    
    else:
        fm = TeachersRegistration()
        print('This is a Get statement')
    return render(request, 'blogs/forms.html', {'form': fm})
