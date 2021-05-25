from django.shortcuts import render
from porfolio.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def resume(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        mess=request.POST.get('message')
        recepient = str(sub['Email'].value())
        try:
            send_mail(subject, mess, email,[EMAIL_HOST_USER])
            messages.success(request,"Your message has been sent")
        except Exception as e:
            messages.success(request,"Your message has not sent")
    return render(request,'contact.html')


# Create your views here.
#DataFlair #Send Email
