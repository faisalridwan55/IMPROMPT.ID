from django.shortcuts import render
from .models import Employer, Company, Opportunity
from .forms import EmployerProfileEdit, CompanyProfileEdit
from app_job_seeker.models import Application_Form
# Create your views here.
response = {}

def home_employer(request):
    # Pastikan yang login employer
    if request.session['status'] == "employer":
        return render(request, 'home_employer.html', response)

def my_company_profile(request):
    if request.session['status'] == "employer":
        company = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
        response['company'] = company
        return render(request, 'company_profile.html', response)

def employer_profile(request):
    if request.session['status'] == "employer":
        employer = Employer.objects.get(company_creator_profile_id=request.session['profile_id'])
        response['employer'] = employer
        return render(request, 'employer_profile.html', response)

def edit_company_profile(request):
    if request.session['status'] == "employer":
        response['company_form'] = CompanyProfileEdit
        return render(request, 'edit_company_profile.html', response)

def edit_employer_profile(request):
    if request.session['status'] == "employer":
        response['employer_form'] = EmployerProfileEdit
        return render(request, 'edit_employer_profile.html', response)

def submit_company_profile(request):
    if request.session['status'] == "employer":
        form = CompanyProfileEdit(request.POST or None)
        if(request.method == 'POST' and form.is_valid()):
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
                company = query[0]
                company.country = country
                company.province = province
                company.city = city
                company.company_name = company_name
                company.company_description = company_description
                company.company_website = company_website
                company.company_logo = company_logo
                company.save()
            else:
                Company.objects.create(
                    company_creator_profile_id=request.session['profile_id'],
                    country = country,
                    province = province,
                    city = city,
                    company_name = company_name,
                    company_description = company_description,
                    company_website = company_website,
                    company_logo = company_logo
                )
        return redirect(reverse('app_employer:company_profile'))

def submit_employer_profile(request):
    form = CompanyProfileEdit(request.POST or None)
    if request.session['status'] == "employer":
        if(request.method == 'POST' and form.is_valid()):
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)

            query = Employer.objects.filter(profile_id=request.session['profile_id'])
            query_size = query.count()
            if query_size > 0:
                employer = query[0]
                employer.first_name = first_name
                employer.last_name = last_name
                employer.email = email
                employer.phone_number = phone_number
                employer.save()
            else:
                Employer.objects.create(
                    profile_id=request.session['profile_id'],
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone_number = phone_number
                )
        return redirect(reverse('app_employer:employer_profile'))

def submit_opportunity_posting(request):
    # opportunity posting nya pake bootstrap modal
    if request.session['status'] == "employer":
        if(request.method == 'POST'):
            opportunity_category = request.POST.get('opportunity_category', False)
            opportunity_field = request.POST.get('opportunity_field', False)
            durations = request.POST.get('durations', False)
            salary = request.POST.get('salary', False)
            participants_needed = request.POST.get('participants_needed', False)
            requirements = request.POST.get('requirements', False)
            description = request.POST.get('description', False)
            contact_person_phone_number = request.POST.get('contact_person_phone_number', False)
            opportunity_owner = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
        return render(request, 'opportunity_posting.html', response)

# Check if the opportunity is ours
def check_applicant(requests, opportunity):
    if request.session['status'] == "employer":
        if opportunity.opportunity_owner.company_creator_profile_id == request.session['profile_id']:
            application_list = Application_Form.objects.filter(opportunity=opportunity)
            return application_list
        else:
            return HttpResponse("null")
    else:
        return HttpResponse("null")
