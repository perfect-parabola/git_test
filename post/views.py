from django.shortcuts import render, redirect
from .models import *
from .forms import*
from django.views.decorators.csrf import csrf_exempt
import ast

# Create your views here.

@csrf_exempt
def main(request):

    context = {'posts': post.objects.all().order_by('-created_at')[0:10]}
    # a = ast.literal_eval(request.body)
    # print(a.get('image'))
    return render(request, 'post/main.html', context)

def create_post1(request):
    if request.method == 'GET':
        form = post_create_form()
        return render(request, 'post/create_form1.html', {'form': form})
    else:
        form = post_create_form(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'post/post_created.html')

def create_post2(request):
    if request.method == 'GET':
        return render(request, 'post/create_form2.html')
    else:

        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        post.objects.create(title=title, author=author, content=content)
        #return render(request, 'post/post_created.html')
        return redirect('post:post_created')

def post_created(request):
    return render(request, 'post/post_created.html')