from django.shortcuts import render, redirect, reverse
from .models import Job_Seeker, Application_Form
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.
response = {}

def home_job_seeker(request):
    if request.session['status'] == "job_seeker":
        response['logged_in'] = True
        return render(request, 'home_job_seeker.html', response)

def edit_profile(request):
    if request.session['status'] == "job_seeker":
        response['logged_in'] = True
        return render(request, 'edit_profile.html', response)

@csrf_exempt
def submit_job_seeker_profile(request):
    if request.session['status'] == "job_seeker":
        print("berhasil")
        if(request.method == 'POST'):
            print("masuk save")
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
            return redirect(reverse('app-job-seeker:home-job-seeker'))

def apply(request):
    if request.session['status'] == "job_seeker":
        id_opportunity = request.POST.get('id_opportunity', False)
        current_job_seeker = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
        current_opportunity = Opportunity.objects.get(pk=id_opportunity)
        Application_Form.objects.create(job_seeker=current_job_seeker, opportunity=current_opportunity)
        return HttpResponse("applied")
    else:
        return HttpResponse("can not apply")
