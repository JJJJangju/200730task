from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone

def renew(request,post_id):
    post_r=get_object_or_404(Post,pk=post_id)
    return render(request,'renew.html',{'post':post_r})

def delete(request,post_id):
    post_d=get_object_or_404(Post,pk=post_id)
    post_d.delete()
    return redirect('/')     


def upload(request):
    return render(request,'new.html')

def create(request):
    form=Post()
    form.title=request.POST['title']
    form.body=request.POST['body']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('/')

def main(request):
    main=Post.objects.all()
    return render(request,'main.html',{'main':main})

def update(request,post_id):
    form=get_object_or_404(Post,pk=post_id)
    form.title = request.POST['title']
    form.body = request.POST['body']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('/detail/' + str(form.id))

def detail(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    return render(request,'detail.html',{'post':post})