from django.shortcuts import render
from .models import Imprompt_Profile
# Create your views here.
response = {}

def home_public(request):
    return render(request, 'home_public.html', response)

def about_company(request):
    company_profile = Company_Profile.objects.get(status=True)
    response['baris_atas'] = company_profile.baris_atas
    response['baris_bawah'] = company_profile.baris_bawah
    return render(request, 'about_company.html', response)

def news_page(request):
    return render(request, 'news_page.html', response)

def news_detail(request, pk):
    # Ambil objek dari database
    return render(request, 'news_detail.html', response)

def opportunity_page(request, id):
    if id == 1:
        # Ambil kumpulan opportunity dari masing2 db
        pass
    elif id == 2:
        # Ambil kumpulan opportunity dari masing2 db
        pass
    elif id == 3:
        # Ambil kumpulan opportunity dari masing2 db
        pass
    elif id == 4:
        # Ambil kumpulan opportunity dari masing2 db
        pass
    return render(request, 'opportunity_page.html', response)

def opportunity_detail(request, id, pk):
    if id == 1:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
        pass
    elif id == 2:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
        pass
    elif id == 3:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
        pass
    elif id == 4:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
        pass
    return render(request, 'opportunity_detail.html', response)
