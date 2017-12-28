from django.shortcuts import render,HttpResponse,reverse,HttpResponseRedirect
from .models import Posts
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='/users/user-login/')
def posts_list(request):
    posts=None
    q=request.GET.get("q",None)

    if q:
        posts = Posts.objects.filter(Q(user__username=q)|Q(title__icontains=q)|Q(content__icontains=q)) #tüm postları çektik.
    else:
        posts=Posts.objects.all()
    return render(request,"posts/post_index.html",context={"posts":posts})

def post_detay(request,pk):
    comment_form = CommentForm()
    post = Posts.objects.get(id=pk)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post = post
            comment.user =request.user
            comment.save()

    return render(request,"posts/post-detail.html",context={"post":post,'form':comment_form})

def post_create(request):
    post_form = PostForm()
    if request.method == "POST":
        post_form=PostForm(data=request.POST,files=request.FILES)
        post = post_form.save(commit=False)
        post.user=request.user
        post.save()
        return HttpResponseRedirect(reverse('post-list'))
    return render(request,'posts/post-create.html',context={'form':post_form})


def post_update(request,pk):
    post = Posts.objects.get(id=pk)
    if not post.user == request.user:
        return HttpResponseRedirect(reverse('post-list'))
    post_form = PostForm(instance=post)
    if request.method == "POST":
        post_form=PostForm(data=request.POST,instance=post)
        post_form.save(commit=True)
        return HttpResponseRedirect(reverse('post-detay',kwargs={'pk':post.id}))
    return render(request,'posts/post_update.html',context={'form':post_form})

def post_delete(request,pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    return HttpResponseRedirect(reverse('post-list'))

@login_required(login_url='/users/user-login/')
def my_post_list(request):
   # ali = Posts.objects.all() #tüm postları çektik.
    post=Posts.objects.filter(user=request.user)
    return render(request,'posts/my-posts.html',context={'posts':post})









