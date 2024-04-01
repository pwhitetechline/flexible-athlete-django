from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from markdownx.utils import markdownify
from django.shortcuts import get_object_or_404


def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by('-published_date')
    else:
        posts = Post.objects.all().order_by('-published_date')

    # Show 5 posts per page
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    for post in posts:
        post.content = markdownify(post.content)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = markdownify(post.content)  # Convert Markdown content to HTML
    return render(request, 'blog/post_detail.html', {'post': post})

