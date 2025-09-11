from django.shortcuts import render
from django.contrib import messages
from .models import *
# Create your views here.



def index(request):
    return render(request, 'index.html')

    

def about(request):
    return render(request, 'about.html')




def service(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        
        contacts = Contact(
            name = name,
            email = email,
            message = message,
            number = number,
        )
        contacts.save()
        messages.success(request, 'We received your message, we will contact you soon !!!')
    contact = Contact.objects.all() 
    context = {
        "contacts":contact
    }  
        
    return render(request, 'contact.html', context)

def track(request):

    if request.method == "GET" and "tracking-number" in request.GET:
        number = request.GET.get("tracking-number")
        items = Shipment.objects.filter(tracking_number=number)

        if items:
            context = {
                "number": number,
                "items": items,
            }
            return render(request, "track.html", context)
        else:
            messages.error(request, 'Not Found')

    return render(request, "track.html")