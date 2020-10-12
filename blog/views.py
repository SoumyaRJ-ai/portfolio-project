from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    blogs = Blog.objects.all
    title = "Blogs"
    return render(request, 'blog/allblogs.html', {'blogs': blogs, 'title':title})


def detailblog(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    title = detailblog.title
    return render(request, 'blog/detail.html', {'blog': detailblog, 'title':title})