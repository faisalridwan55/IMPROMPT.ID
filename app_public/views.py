from django.shortcuts import render

# Create your views here.
response = {}

def home_public(request):
    return render(request, 'home_public.html', response)

def about_company(request):
    return render(request, 'about_company.html', response)

def news_page(request):
    return render(request, 'news_page.html', response)

def news_detail(request, pk):
    # Ambil objek dari database
    return render(request, 'news_detail.html', response)

def opportunity_page(request, id):
    if id == 1:
        # Ambil kumpulan opportunity dari masing2 db
    else if id == 2:
        # Ambil kumpulan opportunity dari masing2 db
    else if id == 3:
        # Ambil kumpulan opportunity dari masing2 db
    else if id == 4:
        # Ambil kumpulan opportunity dari masing2 db
    return render(request, 'opportunity_page.html', response)

def opportunity_detail(request, id, pk):
    if id == 1:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
    else if id == 2:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
    else if id == 3:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
    else if id == 4:
        # Ambil kumpulan opportunity dari masing2 db dengan pk terkait
    return render(request, 'opportunity_detail.html', response)
