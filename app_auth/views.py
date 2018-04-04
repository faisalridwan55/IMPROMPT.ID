from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from app_employer.models import Employer
from app_job_seeker.models import Job_Seeker
import requests

# Create your views here.
response = {}

def login_page(request):
    response['login_page'] = True
    response['about'] = False
    response['news_page'] = False
    response['home'] = False
    response['opportunity_page'] = False
    return render(request, 'login_page.html', response)

@csrf_exempt
def login(  request):
    profile_id = request.POST.get('profile_id', False)
    first_name = request.POST.get('first_name', False)
    last_name = request.POST.get('last_name', False)
    email = request.POST.get('email', False)
    status = request.POST.get('status', False)
    print(profile_id + " " + first_name + " " + last_name + " " + email + " " + status)
    request.session['profile_id'] = profile_id

    # Employer login
    if status == "employer":
        # Check sudah pernah login belum
        query = Employer.objects.filter(profile_id=profile_id)
        query_size = query.count()
        request.session['status'] = "employer"
        # Kalo belum ada di db
        if query_size == 0:
            Employer.objects.create(profile_id=profile_id, first_name=first_name, last_name=last_name, email=email)
            # return redirect(reverse('app_employer:edit_company_profile'))
            return HttpResponse("employer baru")
        return HttpResponse("employer lama")

    # Job Seeker login
    if status == "job_seeker":
        # Check sudah pernah login belum
        query = Job_Seeker.objects.filter(profile_id=profile_id)
        query_size = query.count()
        request.session['status'] = "job_seeker"
        # Kalo belum ada di db
        if query_size == 0:
            Job_Seeker.objects.create(profile_id=profile_id, first_name=first_name, last_name=last_name, email=email)
            # return redirect(reverse('app_job_seeker:edit_profile'))
            return HttpResponse("job_seeker baru")
        return HttpResponse("job_seeker lama")
    return HttpResponse("berhasil umum")
