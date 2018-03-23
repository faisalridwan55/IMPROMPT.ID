from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from app_employer.models import Employer
import requests

# Create your views here.
response = {}

def index(request):
    return render(request, 'home_page.html', response)

def test(request):
    return render(request, 'test.html', response)

@csrf_exempt
def login(request):
    # .get('is_private', False)
    # print(request.POST['profile_id'])
    profile_id = request.POST.get('profile_id', False)
    full_name = request.POST.get('full_name', False)
    email = request.POST.get('email', False)
    status = request.POST.get('status', False)

    # Employer login
    if status == "employer":
        # Check sudah pernah login belum
        query = Employer.objects.filter(profile_id=profile_id)
        print(query.count())
        query_size = query.count()

        # Kalo belum ada di db
        if query_size == 0:
            Employer.objects.create(profile_id=profile_id, name=full_name, email=email)
            return redirect(reverse('app_employer:edit'))
    # return redirect('https://www.google.com/')
    return HttpResponse("berhasil")

def test1(request):
    print("test1")
    return redirect('/employer/home')
