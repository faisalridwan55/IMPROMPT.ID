from django.shortcuts import render
from .models import Employer
# Create your views here.
response = {}

def home_employer(request):
    # Pastikan yang login employer
    if request.session['status'] == "employer":
        return render(request, 'home_employer.html', response)

def edit_company_profile(request):
    if request.session['status'] == "employer":
        return render(request, 'edit_company_profile.html', response)

def submit_profile(request):
    if request.session['status'] == "employer":
        if(request.method == 'POST'):
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)

            profile = Employer.objects.get(profile_id=request.session['profile_id'])
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.phone_number = phone_number
            profile.save()

def opportunity_posting(request):
    if request.session['status'] == "employer":
        # Ambil data dari form untuk buat objek opportunity di database
        return render(request, 'opportunity_posting.html', response)
