from django.shortcuts import redirect, render
from.models import Blog
from django.http import HttpResponse
from.forms import BlogForm

# Create your views here.


def index(request):
    blogs=Blog.objects.all()
    context={
    'blogs':blogs
    }
    return render(request,'index.html',context)

def all_blogs(request):
    blogs=Blog.objects.all()
    context={
    'blogs':blogs
    }
    return render(request,'all_blogs.html',context)
    


def blog_detail(request,pk):
    try:
        blogs=Blog.objects.get(pk=pk)     
    except:
        blogs='Bu Idli Blog Tapilmadi'
    context={
    'blogs':blogs
    }
    return render(request,'blog_detail.html',context)


def create_blog(request):
    forms=BlogForm()
    if request.method=='POST' :
        forms=BlogForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('all_blogs')
    context={
    'forms':forms
    }
    return render(request,'create_blog.html',context)

def update_blog(request,pk):
    blog=Blog.objects.get(pk=pk)
    forms=BlogForm(instance=blog)
    
    if request.method=='POST':
        forms=BlogForm(request.POST, instance=blog)
        if forms.is_valid():
            forms.save()
            return redirect('all_blogs')
    context={
        'forms':forms
    }
    return render(request,'update_blog.html',context)

def delete_blog(request,pk):
    blog=Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('all_blogs')




