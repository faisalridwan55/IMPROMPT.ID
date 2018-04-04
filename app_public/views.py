from django.shortcuts import render
from .models import Imprompt_Profile, News
from app_employer.models import Opportunity
# Create your views here.
response = {}

def home_public(request):
    response['home'] = True
    response['news_page'] = False
    response['about'] = False
    response['opportunity_page'] = False

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

def opportunity_page(request, id):
    response['opportunity_page'] = True
    response['home'] = False
    response['about']= False
    response['news_page'] = False
    if id == 1:
        # Ambil kumpulan job dari db
        response['opportunity_list'] = get_opportunity('job')
    elif id == 2:
        # Ambil kumpulan internship dari db
        response['opportunity_list'] = get_opportunity('internship')
    elif id == 3:
        # Ambil kumpulan community dari db
        response['opportunity_list'] = get_opportunity('community')
    elif id == 4:
        # Ambil kumpulan conference dari db
        response['opportunity_list'] = get_opportunity('conference')
    return render(request, 'opportunity_page.html', response)

def opportunity_detail(request, id, pk):
    response['opportunity_page'] = True
    response['home'] = False
    response['about']= False
    response['news_page'] = False
    if id == 1:
        # Ambil kumpulan job dari db
        response['opportunity'] = get_opportunity_detail('job', pk)
    elif id == 2:
        # Ambil kumpulan internship dari db
        response['opportunity'] = get_opportunity_detail('internship', pk)
    elif id == 3:
        # Ambil kumpulan community dari db
        response['opportunity'] = get_opportunity_detail('community', pk)
    elif id == 4:
        # Ambil kumpulan conference dari db
        response['opportunity'] = get_opportunity_detail('conference', pk)
    return render(request, 'opportunity_detail.html', response)

def get_opportunity(request, category):
    opportunity_list = Opportunity.objects.filter(opportunity_category=category)
    return opportunity_list

def get_opportunity_detail(request, category, pk):
    try:
        opportunity = Opportunity.objects.get(opportunity_category=category, pk=pk)
        return opportunity
    except Exception as e:
        pass
