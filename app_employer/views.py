from django.shortcuts import render

# Create your views here.
response = {}

def home(request):
    print('TEST EMPLOYER')
    return render(request, 'home_employer.html', response)
