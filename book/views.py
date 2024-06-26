from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Category
from .forms import BookForm

def index(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_is_authenticated': request.user.is_authenticated,
        'user_is_admin': request.user.is_staff
    }
    return render(request, 'book/index.html', context)

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book,
        'user_is_authenticated': request.user.is_authenticated,
        'user_is_admin': request.user.is_staff
    }
    return render(request, 'book/book_detail.html', context)

@login_required
@permission_required('book.add_book', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    else:
        form = BookForm()
    return render(request, 'book/add.html', {'form': form})

@login_required
@permission_required('book.change_book', raise_exception=True)
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit.html', {'form': form})

@login_required
@permission_required('book.delete_book', raise_exception=True)
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:index')
    return render(request, 'book/delete.html', {'book': book})
