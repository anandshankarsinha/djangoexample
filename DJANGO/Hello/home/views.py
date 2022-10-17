from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):

    context = {
        'variable': "ANAND IS GREAT",
        'variable1': "I LOVE YOU"

    }
    return render(request, 'index.html')
    # return HttpResponse("THIS IS A HOME PAGE ")


def about(request):
   # return HttpResponse("THIS IS ABOUT PAGE ")
    return render(request, 'about.html')


def services(request):
   # return HttpResponse("THIS IS SERVICE PAGE ")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("THIS IS CONTACT PAGE ")
    if request.method == "POST":
        name = request.POST.get('name')
        query = request.POST.get('query')
        phone = request.POST.get('phone')
        contact = Contact(name=name, query=query, phone=phone, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
