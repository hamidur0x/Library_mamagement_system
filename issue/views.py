# issue/views.py
from django.shortcuts import render
from .models import Issue

def issue_history(request):
    issues = Issue.objects.select_related("book").order_by("-issued_at")
    return render(request, "issue/history.html", {"issues": issues})