from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()        #thiss single line of code grabs everything out of Database and convert them into Python Objects and then puts them into a list.
    return render(request, 'portfolio/home.html', {'projects':projects})   