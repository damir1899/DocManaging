from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
import random

from .forms import  AddDocumentForm, UserForm
from .models import Document


def IndexView(request):
    if request.user.is_authenticated:
        data = Document.objects.filter(owner=request.user).order_by('-created_at')
        context = {
                    'data': data
                    }
        return render(request, 'main/index.html', context=context)
    else:
        return redirect('login/')


def DocumentDetailView(request, slug):
    document = get_object_or_404(Document, slug=slug)
    if request.method == 'POST':
        form = AddDocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddDocumentForm(instance=document)
    context = {
        'document': document,
        'form': form
    }
    
    return render(request, 'main/document_detail.html', context=context)


def AddDocumentView(request):
    if request.method == 'POST':
        form = AddDocumentForm(request.POST, request.FILES)
        form.instance.owner = request.user
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddDocumentForm()

    context = {
        'form': form
    }
    return render(request, 'main/add_document.html', context=context)


def DeleteDocumentView(request, post_id=None):
    doc_to_delete=Document.objects.get(id=post_id)
    doc_to_delete.delete()
    return redirect('/')
    
    
def LoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('/')
    return render(request, "auth/login.html")


def SignUpView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                return redirect('/signup')
            else:
                user.set_password(user.password)
                form.save()
                return redirect("/")
    else:
        form = UserForm()
    return render(request, "auth/signup.html", {"form": form})


def LogoutView(request):
    logout(request)
    return redirect("/")
