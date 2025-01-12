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

        mail_message = "Name: " + f"{message_name}\n" + "Email: " + f"{message_email}\n" + "Message: " + message
        #send Email function
        send_mail (
            'New Web Order', mail_message,
            'reply@stacysdoggiedelights.com', #from email
            ['orders@stacysdoggiedelights.com'],
        )
        return render(request, 'thankyou.html', {'message_name' : message_name })

    else:
        return render(request, 'home.html', {})
