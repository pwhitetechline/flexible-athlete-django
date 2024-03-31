from django.shortcuts import render
from .models import Post
from markdownx.utils import markdownify
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    # Convert Markdown content to HTML
    for post in posts:
        post.content = markdownify(post.content)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = markdownify(post.content)  # Convert Markdown content to HTML
    return render(request, 'blog/post_detail.html', {'post': post})

