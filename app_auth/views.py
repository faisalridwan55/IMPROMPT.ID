from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
response = {}

def index(request):
    return render(request, 'home_page.html', response)

@csrf_exempt
def login(request):
    print(request.POST['profile_id'])
    print(request.POST['full_name'])
    print(request.POST['email'])
    print(request.POST['status'])
