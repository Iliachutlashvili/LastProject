from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Category
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/detail.html', {'book': book})

@login_required
@permission_required('book.add_book', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('book:index')
        else:
            print("Form is not valid")
            print(form.errors)  # This will print form errors to the console
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
            return redirect('book:detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit.html', {'form': form, 'book': book})

@login_required
@permission_required('book.delete_book', raise_exception=True)
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:index')
    return render(request, 'book/delete.html', {'book': book})
