from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["owner", "name", "description"]
    list_filter = ["owner", 'created_at']
    search_fields = ["owner"]
    ordering = ['-created_at']
    