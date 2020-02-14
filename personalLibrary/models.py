from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class MyBookCollection(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    readStatus = models.CharField(max_length=200, blank=True, null=True)
    myRating = models.PositiveIntegerField(null=True, default=5)
    myReview = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.book.title


