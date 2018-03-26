from django.shortcuts import render

# Create your views here.
response = {}

def home_employer(request):
    return render(request, 'home_employer.html', response)

def edit_company_profile(request):
    return render(request, 'edit_company_profile.html', response)

def opportunity_posting(request):
    # Ambil data dari form untuk buat objek opportunity di database
    return render(request, 'opportunity_posting.html', response)
