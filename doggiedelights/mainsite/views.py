from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send Email function
        send_mail (
            message_name, #subject
            message,
            message_email,
            ['orders@stacysdoggiedelights.com'],
            fail_silently=False,
        )
        return render(request, 'thankyou.html', {'message_name' : message_name })

    else:
        return render(request, 'home.html', {})
