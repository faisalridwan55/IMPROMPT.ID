from django.shortcuts import render
from .models import Imprompt_Profile, News
from app_employer.models import Opportunity
from app_employer.views import check_applicant
from app_job_seeker.models import Job_Seeker, Application_Form
from .forms import SearchDropdown
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
response = {}

def home_public(request):
    response['home'] = True
    response['news_page'] = False
    response['about'] = False
    response['opportunity_page'] = False
    all_opportunity = Opportunity.objects.all().order_by('-id')
    response['search'] = SearchDropdown
    response['opportunity'] = all_opportunity
    #nanti mau ditambahin paginator kalo udah banyak

    return render(request, 'home_public.html', response)

def about_company(request):
    # Pake try selama belum ngisi db
    try:
        response['about'] = True
        response['news_page'] = False
        response['home'] = False
        response['opportunity_page'] = False
        company_profile = Imprompt_Profile.objects.get(active=True)
        response['baris_atas'] = company_profile.baris_atas
        response['baris_bawah'] = company_profile.baris_bawah
    except Exception as e:
        pass
    return render(request, 'about_company.html', response)

def news_page(request):
    # Pake try selama belum ngisi db
    try:
        response['about'] = False
        response['news_page'] = True
        response['home'] = False
        response['opportunity_page'] = False
        news_list = News.objects.all()
        response['news_list'] = news_list
    except Exception as e:
        pass
    return render(request, 'news_page.html', response)

def news_detail(request, pk):
    # Ambil objek dari database
    # Pake try selama belum ngisi db
    try:
        response['about'] = False
        response['news_page'] = True
        response['home'] = False
        response['opportunity_page'] = False
        news = News.objects.get(pk=pk)
        response['news'] = news
    except Exception as e:
        pass
    return render(request, 'news_detail.html', response)

def opportunity_page(request, categories):
    response['opportunity_page'] = True
    response['home'] = False
    response['about']= False
    response['news_page'] = False
    response['search'] = SearchDropdown
    response['search_result'] = False
    response['category'] = categories
    if categories == 'jobs':
        # Ambil kumpulan job dari db
        response['opportunity_list'] = get_opportunity('jobs')
    elif categories == 'internship':
        # Ambil kumpulan internship dari db
        response['opportunity_list'] = get_opportunity('internship')
    elif categories == 'community':
        # Ambil kumpulan community dari db
        response['opportunity_list'] = get_opportunity('community')
    elif categories == 'conference':
        # Ambil kumpulan conference dari db
        response['opportunity_list'] = get_opportunity('conference')
    elif categories == 'volunteer':
        # Ambil kumpulan conference dari db
        response['opportunity_list'] = get_opportunity('volunteer')
    return render(request, 'opportunity_page.html', response)

def opportunity_detail(request, categories, pk):
    try:
        if request.session['status'] == "job_seeker":
            current_job_seeker = Job_Seeker.objects.get(profile_id=request.session['profile_id'])
            query = Application_Form.objects.filter(job_seeker=current_job_seeker)
            query_size = query.count()
            if query_size > 0:
                response['applied'] = True
            else:
                response['applied'] = False
    except Exception as e:
        pass
    print("pk of opportunity:=>", pk)
    response['opportunity_page'] = True
    response['home'] = False
    response['about']= False
    response['news_page'] = False

    if categories == 'jobs':
        # Ambil kumpulan job dari db
        opportunity = get_opportunity_detail('jobs', pk)
        response['opportunity'] = opportunity
    elif categories == 'internship':
        # Ambil kumpulan internship dari db
        opportunity = get_opportunity_detail('internship', pk)
        response['opportunity'] = opportunity
    elif categories == 'community':
        # Ambil kumpulan community dari db
        opportunity = get_opportunity_detail('community', pk)
        response['opportunity'] = opportunity
    elif categories == 'conference':
        # Ambil kumpulan conference dari db
        opportunity = get_opportunity_detail('conference', pk)
        response['opportunity'] = opportunity
    elif categories == 'volunteer':
        # Ambil kumpulan conference dari db
        opportunity = get_opportunity_detail('volunteer', pk)
        response['opportunity'] = opportunity

    # Kalo yang buka employer dan ini adalah opportunity yang
    # dia posting, maka dia bisa liat applicant
    try:
        application_list = check_applicant(opportunity)
        if application_list != "null":
            response['application_list'] = application_list
    except Exception as e:
        pass
    return render(request, 'opportunity_detail.html', response)

def get_opportunity(category):
    opportunity_list = Opportunity.objects.filter(opportunity_category=category)
    return opportunity_list

def get_opportunity_detail(category, pk):
    try:
        opportunity = Opportunity.objects.get(opportunity_category=category, pk=pk)
        return opportunity
    except Exception as e:
        pass

@csrf_exempt
def search_by_drop_down(request):
    response['search_result'] = True
    opportunity_category = request.POST.get('opportunity_category', False)
    opportunity_field = request.POST.get('opportunity_field', False)

    response['opportunity_category'] = opportunity_category
    response['opportunity_field'] = opportunity_field

    if opportunity_category != "null" and opportunity_field != "null":
        list_opportunity = Opportunity.objects.filter(opportunity_category=opportunity_category, opportunity_field=opportunity_field)
        response['opportunity_list'] = list_opportunity
        return render(request, 'opportunity_page.html', response)
    elif opportunity_category == "null":
        list_opportunity = Opportunity.objects.filter(opportunity_field=opportunity_field)
        response['opportunity_list'] = list_opportunity
        return render(request, 'opportunity_page.html', response)
    elif opportunity_field == "null":
        list_opportunity = Opportunity.objects.filter(opportunity_category=opportunity_category)
        response['opportunity_list'] = list_opportunity
        return render(request, 'opportunity_page.html', response)
    else:
        return HttpResponse("null")
