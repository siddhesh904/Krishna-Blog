from django.shortcuts import render,redirect
from Blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request, 'about.html')

def sign_in(request):
    if(request.method == 'POST'):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username)
        if(not user.exists()):
            messages.error(request, 'Invalid Username')
            return redirect('/sign_in')
        userAuth = authenticate(username = username, password = password)
        if(userAuth is None):
            messages.error(request, 'Invalid Password')
            return redirect('/sign_in')
        else:
            login(request, userAuth)
            return redirect('/')
    return render(request, 'sign_in.html')
    
def sign_out(request):
    if(request.method == 'POST'):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username)
        if(user.exists()):
            messages.info(request, 'Username Alrady exists!')
            return redirect('/sign_out')


        queryset = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        queryset.set_password(password)
        queryset.save()

        messages.info(request, "Acccout Created Sccussfully!")
    return render(request, 'sign_out.html')

def logout_user(request):
    logout(request)
    return redirect('/sign_in')

@login_required(login_url='/sign_in')
def addContent(request):
    if(request.method == 'POST'):
        data = request.POST
        name = data.get('name')
        content = data.get('content')
        images = request.FILES.get('images')

        Blog.objects.create(
            name = name,
            content = content,
            images = images
        )
        print(name)
        print(content)
        print(images)
        return redirect('/addContent')

        
    return render(request, 'AddBlog.html')


def blogInfo(request):
    queryset = Blog.objects.all()
    context = {
        'Info':queryset
    }
    return render(request, 'blog.html',context)


def update(request, id):
    queryset = Blog.objects.get(id = id)
    if(request.method == 'POST'):
        data = request.POST
        name = data.get('name')
        content = data.get('content')
        images = data.get('images')
        
        queryset.name = name
        queryset.content = content
        if(images):
            queryset.images =  images
        queryset.save()
        return redirect('/blog')
    context = {
        'blog':queryset
    }
    return render(request, 'update.html',context)


def delete(request, id):
    queryset = Blog.objects.get(id = id)
    queryset.delete()
    return redirect('/blog')

def viewBlog(request,id):
    queryset = Blog.objects.get(id = id)
    data = [
        {'name' : queryset.name},
        {'content' :queryset.content},
        {'images': queryset.images}
    ]

    context ={
        'newData':data
    }
    return render(request, 'viewBlog.html',context)
    


