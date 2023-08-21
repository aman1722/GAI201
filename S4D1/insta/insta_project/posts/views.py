from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post-list')
