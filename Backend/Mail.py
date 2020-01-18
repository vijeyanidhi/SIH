from django.core.mail import send_mail

def sendMail(subject,message,target):
    send_mail(subject,message,'vijeyanidhi@gmail.com',[target],fail_silently=False,)
