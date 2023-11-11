from django.contrib import admin

# Register your models here.
from .models import Diagnosis, Disease, DiseaseLevel


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image"]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]
    list_per_page = 10
    list_editable = ["description", "image"]
    readonly_fields = ["image"]


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]
    list_per_page = 10
    list_editable = ["description"]


@admin.register(DiseaseLevel)
class DiseaseLevelAdmin(admin.ModelAdmin):
    list_display = ["disease", "level", "description"]
    search_fields = ["disease", "level", "description"]
    list_filter = ["disease", "level", "description"]
    list_per_page = 10
    list_editable = ["level", "description"]
