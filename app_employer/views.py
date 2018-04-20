from django.shortcuts import render, redirect, reverse
from .models import Employer, Company, Opportunity
from .forms import EmployerProfileEdit, CompanyProfileEdit, OpportunityForm
from app_job_seeker.models import Application_Form
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
response = {}

def home_employer(request):
    # Pastikan yang login employer
    if request.session['status'] == "employer":
        response['logged_in'] = True
        response['posting_opportunity'] = False
        response['edit_empl'] = False
        response['edit_comp'] = False
        response['home_employer'] = True
        response['company_profile'] = False
        response['employer_profile'] = False
        response['post_opp'] = OpportunityForm
        company = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
        response['company'] = company
        return render(request, 'home_employer.html', response)

def my_company_profile(request):
    if request.session['status'] == "employer":
        response['logged_in'] = True
        response['posting_opportunity'] = False
        response['edit_empl'] = False
        response['edit_comp'] = False
        response['home_employer'] = False
        response['company_profile'] = True
        response['employer_profile'] = False
        try:
            company = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
            employer = Employer.objects.get(profile_id=request.session['profile_id'])
        except Exception as e:
            return redirect(reverse('app-employer:edit-company-profile'))
        opportunity_list = Opportunity.objects.filter(opportunity_owner=company).order_by('-id')
        response['opportunity_list']=opportunity_list
        response['company'] = company
        response['employer'] = employer
        return render(request, 'company_profile.html', response)

def employer_profile(request):
    if request.session['status'] == "employer":
        response['posting_opportunity'] = False
        response['edit_empl'] = False
        response['edit_comp'] = False
        response['home_employer'] = False
        response['company_profile'] = False
        response['employer_profile'] = True
        response['logged_in'] = True
        response['post_opp'] = OpportunityForm
        employer = Employer.objects.get(profile_id=request.session['profile_id'])
        response['employer'] = employer
        return render(request, 'employer_profile.html', response)

def edit_company_profile(request):
    if request.session['status'] == "employer":
        response['posting_opportunity'] = False
        response['edit_empl'] = False
        response['edit_comp'] = True
        response['home_employer'] = False
        response['company_profile'] = False
        response['company_logo'] = False
        response['employer_profile'] = False
        response['logged_in'] = True
        response['company_form'] = CompanyProfileEdit
        try:
            exist_profile = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
            response['exist_profile'] = exist_profile
            form = CompanyProfileEdit(initial={
                'company_name': exist_profile.company_name,
                'country': exist_profile.country,
                'province':exist_profile.province,
                'city':exist_profile.city,
                'company_description':exist_profile.company_description,
                'company_website':exist_profile.company_website,
                'company_logo':exist_profile.company_logo})
            response['company_form'] = form
        except Exception as e:
            response['exist_profile'] = None
        return render(request, 'edit_company_profile.html', response)

def edit_employer_profile(request):
    if request.session['status'] == "employer":
        response['posting_opportunity'] = False
        response['edit_empl'] = True
        response['edit_comp'] = False
        response['home_employer'] = False
        response['company_profile'] = False
        response['employer_profile'] = False
        response['logged_in'] = True
        response['employer_form'] = EmployerProfileEdit
        try:
            exist_profile = Employer.objects.get(profile_id=request.session['profile_id'])
            response['exist_profile'] = exist_profile
            form = EmployerProfileEdit(initial={
                'first_name': exist_profile.first_name,
                'last_name':exist_profile.last_name,
                'email':exist_profile.email,
                'phone_number':exist_profile.phone_number,
                'profile_picture':exist_profile.profile_picture})
            response['employer_form'] = form
        except Exception as e:
            response['exist_profile'] = None
        return render(request, 'edit_employer_profile.html', response)

@csrf_exempt
def submit_company_profile(request):
    if request.session['status'] == "employer":
        form = CompanyProfileEdit(request.POST, request.FILES)
        if(request.method == 'POST'):
            company_creator_profile_id = request.session['profile_id']
            country = request.POST.get('country', False)
            province = request.POST.get('province', False)
            city = request.POST.get('city', False)
            company_name = request.POST.get('company_name', False)
            company_description = request.POST.get('company_description', False)
            company_website = request.POST.get('company_website', False)

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
                company.company_logo = request.FILES['company_logo'] if 'company_logo' in request.FILES else None
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
                    company_logo = request.FILES['company_logo'] if 'company_logo' in request.FILES else None
                )

            return redirect(reverse('app-employer:home-employer'))

@csrf_exempt
def submit_employer_profile(request):
    if request.session['status'] == "employer":
        form = EmployerProfileEdit(request.POST or None)
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
                employer.profile_picture = request.FILES['profile_picture']
                employer.save()
            else:
                try:
                    Employer.objects.create(
                        profile_id=request.session['profile_id'],
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        phone_number = phone_number,
                        profile_picture=request.FILES['profile_picture']
                    )
                except Exception as e:
                    Employer.objects.create(
                        profile_id=request.session['profile_id'],
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        phone_number = phone_number
                    )
        query = Company.objects.filter(company_creator_profile_id=request.session['profile_id'])
        query_size = query.count()
        if query_size > 0:
            return redirect(reverse('app-employer:employer-profile'))    
        return redirect(reverse('app-employer:edit-company-profile'))


@csrf_exempt
def submit_opportunity_posting(request):
    # opportunity posting nya pake bootstrap modal
    if request.session['status'] == "employer":
        response['logged_in'] = True
        response['posting_opportunity'] = True
        response['edit_empl'] = False
        response['edit_comp'] = False
        response['home_employer'] = False
        response['company_profile'] = False
        response['employer_profile'] = False
        form = OpportunityForm(request.POST or None)
        if(request.method == 'POST' and form.is_valid()):
            response['opportunity_category'] = request.POST.get('opportunity_category', False)
            response['opportunity_field'] = request.POST.get('opportunity_field', False)
            response['durations'] = request.POST.get('durations', False)
            response['salary']= request.POST.get('salary', False)
            response['participants_needed'] = request.POST.get('participants_needed', False)
            response['requirements'] = request.POST.get('requirements', False)
            response['description'] = request.POST.get('description', False)
            response['contact_person_phone_number'] = request.POST.get('contact_person_phone_number', False)
            response['opportunity_owner'] = Company.objects.get(company_creator_profile_id=request.session['profile_id'])
            opp=Opportunity(opportunity_category=response['opportunity_category'],opportunity_field=response['opportunity_field'],durations=response['durations'],salary=response['salary'],participants_needed=response['participants_needed'], requirements=response['requirements'],description=response['description'],contact_person_phone_number=response['contact_person_phone_number'],opportunity_owner=response['opportunity_owner'])
            opp.save()
        return render(request, 'opportunity_posting.html', response)

# Check if the opportunity is ours
def check_applicant(request, opportunity):
    if request.session['status'] == "employer":
        if opportunity.opportunity_owner.company_creator_profile_id == request.session['profile_id']:
            application_list = Application_Form.objects.filter(opportunity=opportunity)
            return application_list
        else:
            return HttpResponse("null")
    else:
        return HttpResponse("null")
