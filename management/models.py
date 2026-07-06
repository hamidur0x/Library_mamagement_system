from django.db import models

class Book(models.Model):
    book_id = models.PositiveIntegerField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    shelf_number = models.CharField(max_length=10)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])