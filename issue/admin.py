from django.contrib import admin
from .models import Issue


@admin.action(description="Mark selected books as returned")
def mark_returned(modeladmin, request, queryset):
    for issue in queryset:
        issue.return_book()


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("student_id", "book", "issued_at", "returned_at")

    autocomplete_fields = ["book"]

    actions = [mark_returned]