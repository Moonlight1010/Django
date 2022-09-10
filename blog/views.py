from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, TwitterProfile
from .forms import PostForm, TwitterProfileForm
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-id')
    form = PostForm(request.POST)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Post successful')
            return redirect('blog-name')
        else:
            form = PostForm()
    else:
        form = PostForm()
    context = {
        'posts':posts,
        'form': form
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    my_name = 'Stella'
    return render(request, 'blog/about.html', {'my_name':my_name})

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')

def read(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post,id=id)
    context = {
        'post':post,
    }
    return render(request, 'blog/read.html', context)

def myform(request):
    return render(request, 'blog/myform.html')

def update(request, id):
    post = get_object_or_404(Post,id=id)
    form = PostForm(request.POST, instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-read',id=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'blog/update.html', context)
def myform(request):
    twitterprofiles = TwitterProfile.objects.all().order_by('-id')
    paginator = Paginator(twitterprofiles, 2)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    form = TwitterProfileForm(request.POST)
    if request.method == 'POST':
        form = TwitterProfileForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('blog-myform')
        else:
            form = TwitterProfileForm()
    else:
        form = TwitterProfileForm()
    context = {
        'profiles': paged_post,
        'form':form
    }
    return render(request, 'blog/myform.html', context)

def pen(request, id):
        comment = TwitterProfile.objects.get(id=id)
        form = TwitterProfileForm(request.POST, instance=comment)
        if request.method == 'POST':
          form = TwitterProfileForm(request.POST, instance=comment)
          if form.is_valid():
            form.save()
            return redirect('blog-myform')
        else:
            form = TwitterProfileForm(instance=comment)

        context = {
            'form':form,
            'comment':comment
        }
        return render(request, 'blog/pen.html', context)
def penread(request, id):
    profile = TwitterProfile.objects.get(id=id)
    context = {
        'profile':profile
    }
    return render(request, 'blog/penread.html', context)

def delete_view(request, id):
    profile = TwitterProfile.objects.get(id=id)
    profile.delete()
    return redirect('blog-myform')

def search(request):
    profiles = TwitterProfile.objects.all().order_by('-id')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            profiles = profiles.filter(comment__icontains=keyword)
    context = {
        'profiles':profiles,
    }
    return render(request,'blog/search.html',context)