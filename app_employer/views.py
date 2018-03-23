from django.shortcuts import render

# Create your views here.
response = {}

def home(request):
    return render(request, 'home_employer.html', response)

def edit_company_profile(request):
    return render(request, 'edit_company_profile.html', response)
