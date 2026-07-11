from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def machine_learning(request):
    Teachers = {'names': ['Shakil', 'Mejba', 'Sohanur Rahman']}
    # course = 'Machine Learning'
    # Tclass= 21
    # seat =20
    # cduration = '2.5 Months'
    # offering = {'c': course, 'tl' : Tclass, 'st' : seat, 'cd' : cduration}
    return render(request, 'machine_learning/machine_learning.html', context=Teachers)




def random(request):
    return render(request, 'machine_learning/random_forest.html')


def K_nearest(request):
    return render(request, 'machine_learning/knn.html')

def dtree(request):
    return render(request, 'machine_learning/DT.html')

