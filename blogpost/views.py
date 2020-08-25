from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogpost.models import Post,Blogcomment
from django.contrib import messages

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog.html',{"posts":posts})

def savepost(request,slug):
    return render(request,'savepast.html')

def viewpost(request,slug):
    filterpost = Post.objects.filter(slug=slug)
    # comments = Blogcomment.objects.filter(post = post)
    context={"filterpost":filterpost}
    return render(request,'viewpost.html',context)

def postcomment(request,slug):
    if request.method =='POST':
        comment = request.POST.get('comment')
        user= request.user
        postsno = request.POST.get['postsno']
        post = Post.objects.get(sno=postsno)

        comm = Blogcomment(comment=comment,user=user,post=post)
        comm.save()
        messages.success(request,"Your Comment has been posted sucessfully.")

    return redirect('/blogpost/viewpost/{post.slug}')

def deletepost(request,slug):
    return render(request,'deletepost.html')
