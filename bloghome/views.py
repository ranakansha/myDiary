from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogpost.models import Post
from django.contrib import messages
from bloghome.models import Contact
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    return render(request,'index.html')

def mydiaryabout(request):
    return render(request,'about.html')

def mydiarycontact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
        contact.save()
        messages.success(request,'Your Request is in our database.We will contact you within 24 hours.Check your email for further information.')
        return redirect('/bloghome/contact')

    return render(request,'contact.html')

def mydiaryserch(request):
    query = request.GET['query']
    if len(query) >100:
        posts = Post.objects.none()   
    poststitle=Post.objects.filter(post_title__icontains=query)
    postcontent=Post.objects.filter(post_desc__icontains=query)
    posts = poststitle.union(postcontent)
    if posts.count()==0:
        messages.error(request,"No Search Results Found . Please Refine Your Query.")
    return render(request,'search.html',{"posts":posts,"query":query})
    
