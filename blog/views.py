from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blog(request):
    all_post = Paginator(Post.objects.filter(published=True).order_by('-timestamp'), 6)
    page = request.GET.get('page')
    try:
        allPosts = all_post.page(page)
    except PageNotAnInteger:
        allPosts = all_post.page(1)
    except EmptyPage:
        allPosts = all_post.page(all_post.num_pages)

    context = {'allPosts': allPosts}
    return render(request, 'blog/blog.html', context)
    # return HttpResponse('This is Blog Page')

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogpost.html', context)
    # return HttpResponse(f'This is blog post of {slug}')