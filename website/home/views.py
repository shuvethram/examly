from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import courses,student_id
# Create your views here.
def home(request):
    allcourse = courses.objects.all()
    return render(request, 'index.html',{'allcourse':allcourse})
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        courselist = request.POST.getlist('courses')
        for i in range(len(courselist)):
            courselist[i] = courselist[i][0:-2]
        return redirect('profile')
        