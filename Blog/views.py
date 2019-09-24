from django.shortcuts import render, render_to_response
from Blog.models import *
from Blog.forms import CommentForm
from django.http import Http404

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('blog_list.html', {'blogs': blogs})

def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        tags = blog.tags.all()
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments':  blog.comment_set.all().order_by('-created'),
        'form': form,
        'tags': tags,
    }
    return render(request, 'blog_details.html', ctx)
