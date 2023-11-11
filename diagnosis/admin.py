from django.contrib import admin

# Register your models here.
from .models import Diagnosis


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description']
    list_per_page = 10
    list_editable = ['description', 'image']
    readonly_fields = ['image']
