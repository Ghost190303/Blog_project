from django.shortcuts import render
from .models import Blog
from .forms import Blog_Form , UserRegistration
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def Blog_list(request):
    blogs = Blog.objects.all().order_by('-Created_at')
    return render(request, 'app/Blog_list.html', {'blogs': blogs})
@login_required
def Blog_create(request):
    if request.method == 'POST':
        form = Blog_Form(request.POST, request.FILES)   
        if form.is_valid():
            log=form.save(commit=False)
            log.User= request.user
            log.save()
            return redirect('Blog_list')
    else:
        form = Blog_Form()
    return render(request,'app/Blogform.html', {'form':form})
@login_required
def Blog_edit(request, Blog_id):
    blog=get_object_or_404(Blog , pk=Blog_id, User=request.user)
    if request.method == 'POST':
        form = Blog_Form(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            kai=form.save(commit=False)
            kai.User= request.user
            kai.save()
            return redirect('Blog_list')
    else:
        form = Blog_Form(instance=blog)
    return render(request,'app/Blogform.html', {'form':form})

@login_required
def Blog_delete(request, Blog_id):
    blog = get_object_or_404(Blog, pk=Blog_id, User=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('Blog_list')
    return render(request,'app/Blog_confirm_delete.html', {'blog':blog})
    

def registor(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('Blog_list')
    else:
        form = UserRegistration()
    return render(request, 'registration/registor.html', {'form':form})
    

# def forget_password(request):
#     if request.method == 'POST':
#         email=request.post.get('email')

#         if User.objects.filter(email=email).exists():
#             print("user exists")
            
#             return render(request,'registration/forgetpassword.html')