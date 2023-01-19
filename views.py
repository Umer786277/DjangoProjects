from django.shortcuts import render
from.models import Post

# Create your views here.

def index(request):
    return render(request,'home.html')


def services(request):
    return render(request,'services.html')



def contact(request):
    return render(request,'contact.html')


def blog(request):
    posts=Post.objects.all()

    return render(request,'blog.html',{'posts':posts})



def about(request):
    return render(request,'about.html')