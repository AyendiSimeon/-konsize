from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.core.paginator import Paginator

def homeview(request):
    post = Post.objects.all()
    cat = Category.objects.all()
    active = Post.objects.filter(active=True)

    p = Paginator(Post.objects.all(), 2)
    page = request.GET.get('page')
    posts = p.get_page(page)
    context = {
        'post':post,
        'cat':cat,
        'active':active,
        'posts':posts,
    }
    return render(request, 'index/home.html', context)

def PostDetail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.all()
    cat = Category.objects.all()
    #comment = Post.objects.filter(comments=comments)
    context = {
        
        'post':post,
        'posts':posts,
        'cat':cat,
        #'comment':comment,
        
    }
    return render(request, 'index/post_detail.html', context)

def CategoryList(request, slug):
    cat = Category.objects.all()
    cats = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category__slug=slug)
    posts = Post.objects.all()
    context = {
        'cats':cats,
        'cat':cat,
        'post':post,
        'posts':posts,

    }
    return render(request, 'index/categorylist.html', context)

def About(request):
    context = {

    }
    return render(request, 'index/about.html', context)
def Terms(request):
    context = {

    }
    return render(request, 'index/terms.html', context)