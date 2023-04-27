from django.shortcuts import render
from django.http.import HttpResponse
from faculty.models import FacultyInfo
# Create your views here.

def home(request):
	context = {'name' : 'Genna Wood'}
	return render(request, 'faculty/home.html', context)
	#return HttpResponse('<h1>Home Page</h1>')
def getfacultyinfo(request)
	facultydata = FacultyInfo.objects.all()
	context = {'data': facultydata}
	return render(request, 'faculty/facultyinfo.html', context)
