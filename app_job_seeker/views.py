from django.shortcuts import render, redirect, reverse
from .models import Job_Seeker
# Create your views here.
response = {}

def home_job_seeker(request):
    if request.session['status'] == "job_seeker":
        return render(request, 'home_job_seeker.html', response)

def edit_profile(request):
    if request.session['status'] == "job_seeker":
        return render(request, 'edit_profile.html', response)

def submit_profile(request):
    if request.session['status'] == "job_seeker":
        if(request.method == 'POST'):
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)
            birthday = request.POST.get('birthday', False)

            profile = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.phone_number = phone_number
            profile.birthday = birthday
            profile.save()
