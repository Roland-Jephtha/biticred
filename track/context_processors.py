from .models import Phone


def phones(request):

    phones = Phone.objects.all()


    context = {
        'phones' : phones
   
    }

    return context


    