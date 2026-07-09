from django.db import models, transaction
from django.utils import timezone
from management.models import Book


class Issue(models.Model):
    student_id = models.CharField(max_length=5)
    student_name = models.CharField(max_length=100)
    semester = models.CharField(
    max_length=3,
    choices=[
        ("1st", "1st"), ("2nd", "2nd"), ("3rd", "3rd"), ("4th", "4th"),
        ("5th", "5th"), ("6th", "6th"), ("7th", "7th"), ("8th", "8th"),
    ])
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
    shift = models.CharField(
        max_length=10,
        choices=[
            ("Morning", "Morning"),
            ("Day", "Day"),
        ])
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    issued_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding:
                book = Book.objects.select_for_update().get(pk=self.book_id)
                if book.available_copies <= 0:
                    raise ValueError("No copies available.")

                book.available_copies -= 1
                book.save(update_fields=["available_copies"])

            super().save(*args, **kwargs)

    def return_book(self):
        if self.returned_at is not None:
            return

        with transaction.atomic():
            book = Book.objects.select_for_update().get(pk=self.book_id)
            book.available_copies += 1
            book.save(update_fields=["available_copies"])

            self.returned_at = timezone.now()
            super().save(update_fields=["returned_at"])

    def __str__(self):
        return f"{self.student_id} - {self.book}"