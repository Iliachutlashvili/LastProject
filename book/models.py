from django.db import models
from datetime import date
from author.models import Author


class Book(models.Model):
    WANTED = 'wanted'
    WAITING = 'waiting'
    READING = 'reading'
    READ = 'read'

    STATUS_CHOICES = (
        (WANTED, 'Wanted'),
        (WAITING, 'Waiting'),
        (READING, 'Reading'),
        (READ, 'Read')
    )
    
    CATEGORY_CHOICES = [
        ('Trending', 'Trending'),
        ('Classic', 'Classic'),
        ('Love', 'Books We Love'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField(blank=True)
    published_date = models.DateField(default=date.today)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=WAITING)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
