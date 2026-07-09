from django.db import models
class Book(models.Model):
    book_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    department = models.CharField(
    max_length=100,
    choices=[
        ("Computer Science and Technology", "Computer Science and Technology"),
        ("Mechanical Technology", "Mechanical Technology"),
        ("Electrical Technology", "Electrical Technology"),
        ("Electronics Technology", "Electronics Technology"),
        ("Civil Technology", "Civil Technology"),
        ("Electro-medical Technology", "Electro-medical Technology"),
        ("RAC Technology", "RAC Technology"),
        ("Non-Tech", "Non-Tech"),
    ])
    shelf_number = models.CharField(
    max_length=10,
    choices=[
    ("A1", "A1"),
    ("A2", "A2"),
    ("A3", "A3"),
    ("B1", "B1"),
    ("B2", "B2"),
    ("B3", "B3"),
    ("C1", "C1"),
    ("C2", "C2"),
    ("C3", "C3"),
    ("D1", "D1"),

    ])
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('unavailable', 'Unavailable')],
    )

    def __str__(self):
        return self.title