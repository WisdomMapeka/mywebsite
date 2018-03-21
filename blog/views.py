from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quotes, Post


def index(request):
	post = Post.objects.all()
	email = 'wisema27@gmail.com'
	return render(request, 'blog/index.html', {'post':post,  'email':email})


def first(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/first.html', {'posts':posts, 'email':email})

def one(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/one.html', {'posts':posts, 'email':email})


def two(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/two.html', {'posts':posts, 'email':email})

def three(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/three.html', {'posts':posts, 'email':email})

def four(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/four.html', {'posts':posts, 'email':email})

def five(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/five.html', {'posts':posts, 'email':email})

def six(request, pk):
	posts = get_object_or_404(Post, id=pk)
	email = 'wisema27@gmail.com'
	return render(request, 'blog/six.html', {'posts':posts, 'email':email})

