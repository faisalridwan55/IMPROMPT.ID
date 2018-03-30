from django.shortcuts import render
from .models import Employer, Company
# Create your views here.
response = {}

def home_employer(request):
    # Pastikan yang login employer
    if request.session['status'] == "employer":
        return render(request, 'home_employer.html', response)

def company_profile(request):
    if request.session['status'] == "employer":
        return render(request, 'company_profile.html', response)

def employer_profile(request):
    if request.session['status'] == "employer":
        return render(request, 'employer_profile.html', response)

def edit_company_profile(request):
    if request.session['status'] == "employer":
        return render(request, 'edit_company_profile.html', response)

def edit_employer_profile(request):
    if request.session['status'] == "employer":
        return render(request, 'edit_employer_profile.html', response)

def submit_company_profile(request):
    if request.session['status'] == "employer":
        if(request.method == 'POST'):
            company_creator_profile_id = request.session['profile_id']
            country = request.POST.get('country', False)
            province = request.POST.get('province', False)
            city = request.POST.get('city', False)
            company_name = request.POST.get('company_name', False)
            company_description = request.POST.get('company_description', False)
            company_website = request.POST.get('company_website', False)
            company_logo = request.POST.get('company_logo', False)

            query = Company.objects.filter(company_creator_profile_id=request.session['profile_id'])
            query_size = query.count()
            if query_size > 0:
                profile = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
                profile.first_name = first_name
                profile.last_name = last_name
                profile.email = email
                profile.phone_number = phone_number
                profile.save()
            else:
                Employer.objects.create(
                    company_creator_profile_id=request.session['profile_id'],
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone_number = phone_number
                )
        return redirect(reverse('app_employer:company_profile'))

def submit_employer_profile(request):
    if request.session['status'] == "employer":
        if(request.method == 'POST'):
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)

            query = Employer.objects.filter(profile_id=request.session['profile_id'])
            query_size = query.count()
            if query_size > 0:
                profile = Employer.objects.get(profile_id=request.session['profile_id'])
                profile.first_name = first_name
                profile.last_name = last_name
                profile.email = email
                profile.phone_number = phone_number
                profile.save()
            else:
                Employer.objects.create(
                    profile_id=request.session['profile_id'],
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone_number = phone_number
                )
        return redirect(reverse('app_employer:employer_profile'))

def opportunity_posting(request):
    if request.session['status'] == "employer":
        # Ambil data dari form untuk buat objek opportunity di database
        return render(request, 'opportunity_posting.html', response)
