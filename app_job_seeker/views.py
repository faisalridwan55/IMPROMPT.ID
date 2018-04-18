from django.shortcuts import render, redirect, reverse
from .models import Job_Seeker, Application_Form
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from app_employer.models import Opportunity
# Create your views here.
response = {}

def home_job_seeker(request):
    if request.session['status'] == "job_seeker":
        response['jobseeker'] = True
        return render(request, 'home_job_seeker.html', response)

def jobseeker_profile(request):
    if request.session['status'] == "job_seeker":
        response['jobseeker'] = True
        try:
            jobseeker = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
            my_opportunities = Application_Form.objects.filter(job_seeker=jobseeker)
            response['my_opportunities'] = my_opportunities
        except Exception as e:
            response['my_opportunities'] = None
            return redirect(reverse('app-job-seeker:edit-profile'))

        response['data_jobseeker'] = jobseeker
        return render(request, 'my_profile.html', response)

def edit_profile(request):
    if request.session['status'] == "job_seeker":
        response['jobseeker'] = True
        response['form_profile'] = ProfileEdit
        try:
            exist_profile = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
            response['exist_profile'] = exist_profile
            form = ProfileEdit(initial={'first_name': exist_profile.first_name, 'last_name':exist_profile.last_name, 'email':exist_profile.email, 'birthday':exist_profile.birthday, 'phone_number':exist_profile.phone_number})
            response['form_profile'] = form

        except Exception as e:
            response['exist_profile'] = None

        return render(request, 'edit_profile.html', response)

@csrf_exempt
def submit_job_seeker_profile(request):
    if request.session['status'] == "job_seeker":
        form = ProfileEdit(request.POST or None)
        print("berhasil")
        if(request.method == 'POST' and form.is_valid()):
            print("masuk save")
            profile_picture = request.POST.get('profile_picture', False)
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)
            birthday = request.POST.get('birthday', False)
            resume = request.POST.get('resume', False)

            profile = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
            profile.profile_picture = profile_picture
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.phone_number = phone_number
            profile.birthday = birthday
            profile.resume = resume
            profile.save()
            return redirect(reverse('app-public:home-public'))

@csrf_exempt
def apply_opportunity(request, categories, pk):
    if request.session['status'] == "job_seeker":
        id_opportunity = request.POST.get('id_opportunity', False)
        current_job_seeker = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
        current_opportunity = Opportunity.objects.get(pk=id_opportunity)
        Application_Form.objects.create(job_seeker=current_job_seeker, opportunity=current_opportunity)
        return HttpResponse("applied")
    else:
        return HttpResponse("can not apply")
