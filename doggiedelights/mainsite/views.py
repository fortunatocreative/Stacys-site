from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request, 'home.html', {'message_name' : message_name })
        '''
        #send Email function
        send_mail (
            message_name, #subject
            message, 
            message_email,
            ['orders@stacysdoggiedelights.com'],
            fail_silently=False,
        )
        '''
    else:
        return render(request, 'home.html', {})
