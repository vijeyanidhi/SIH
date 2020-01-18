from django.core.mail import send_mail

def sendMail(subject,message,target):
    send_mail(subject,message,'vijeyanidhi@gmail.com',['transfervijay@gmail.com'],fail_silently=False,)
