from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
def email_send(request):
    subject='HI, Hello World!'
    email_message=str(random.randint(100000,999999))
    From_mail=settings.EMAIL_HOST_USER
    to_list=['anushaakula82@gmail.com','anushaanu2826@gmail.com']
    send_mail(subject,email_message,From_mail,to_list,fail_silently=False)
    return HttpResponse("email send successfully")
