import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Author(models.Model):

    first_name = models.CharField(max_length=100, help_text="Enter author first name")
    last_name = models.CharField(max_length=100, help_text="Enter author lastname")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Book(models.Model):

    title = models.CharField(max_length=250, help_text="Enter book title")
    author = models.ForeignKey(Author, models.SET_NULL,null=True)
    summary = models.CharField(max_length=1500, help_text="Enter book description")
    genre = models.ManyToManyField(Genre)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_back = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, models.SET_NULL, null=True, help_text="Choose a book")

    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('o', 'On Loan'),
        ('n', 'Not in stock')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='n', help_text='Availability')
    borrower = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['due_back'],
        permissions = (("can_mark_returned", "Set book as returned"),)

    @property
    def is_overdue(self):
        return self.due_back and self.due_back < datetime.date.today()

    def __str__(self):
        return f"{self.book.title} due back {self.due_back} {self.id}"
# PascalCase C# camel_case python


# class MyModelName(models.Model):
#     """
#     A typical class defining a model, derived from the Model class.
#     """
#
#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
#     ...
#
#     # Metadata
#     class Meta:
#         ordering = ["-my_field_name"]
#
#
#     # Methods
#     def get_absolute_url(self):
#          """
#          Returns the url to access a particular instance of MyModelName.
#          """
#          return reverse('model-detail-view', args=[str(self.id)])
#
#     def __str__(self):
#         """
#         String for representing the MyModelName object (in Admin site etc.)
#         """
#         return self.field_name
