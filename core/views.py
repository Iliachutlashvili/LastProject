from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from book.models import Book


def custom_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    trending_books = Book.objects.filter(category='Trending')
    classic_books = Book.objects.filter(category='Classic')
    books_we_love = Book.objects.filter(category='Love')
    return render(request, 'core/index.html', {
        'trending_books': trending_books,
        'classic_books': classic_books,
        'books_we_love': books_we_love,
    })
def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'core/profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})
