

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=85, blank=True)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Genre(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    CHOICES = (
        ('in stock', 'In stock'),
        ('out os stock', 'Out of stock'),
    )
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True, upload_to='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='books')
    genre = models.ManyToManyField(Genre)
    status = models.CharField(max_length=50, choices=CHOICES, default='default status')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        from django.urls import  reverse
        return reverse('home')

