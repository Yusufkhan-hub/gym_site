from django.shortcuts import render
from .forms import signupForm, galleryForm, feedbackForm
from .models import signUp, gallery
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def content(request):
    return render(request,'content.html')

def gallery(request):
    files = galleryForm()
    if request.method == 'POST':
        files = galleryForm(request.POST,request.FILES)
        if files.is_valid():
            files.save()
            return render(request,'gallery.html')
        else:
            return HttpResponse("""Your form is wrong""")   
    return render(request,'gallery.html',{'file':files})

def instructor(request):
    return render(request,'instructor.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return render(request,'index.html')
    else:
        form = signupForm()
    return render(request,'signup.html',{'form':form})

def create_user(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'signup.html')
    else:
        form = signupForm()
        return render(request,'signup.html',{'form':form})

def about(request):
    return render(request,'about.html')

def why_fit_hit(request):
    feedback = feedbackForm()
    if request.method == 'POST':
        feedback = feedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            return render(request,'whyfitHit.html')
        else:
            return HttpResponse(""" Your feedback is wrong please correct the info""")
    return render(request,'whyfitHit.html',{'feedback':feedback})

