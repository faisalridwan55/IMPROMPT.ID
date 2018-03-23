from django.shortcuts import render, redirect, reverse

# Create your views here.
response = {}

def home(request):
    return render(request, 'home_job_seeker.html', response)

def edit_profile(request):
    return render(request, 'edit_profile.html', response)
