from django.contrib import admin

# Register your models here.
from .models import Diagnosis, Disease, DiseaseLevel


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["name", "result", "description", "image", "created_at", "updated_at"]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]
    list_per_page = 10
    readonly_fields = ["image"]


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]
    list_per_page = 10


@admin.register(DiseaseLevel)
class DiseaseLevelAdmin(admin.ModelAdmin):
    list_display = ["disease", "level", "description", "created_at", "updated_at"]
    search_fields = ["disease", "level", "description"]
    list_filter = ["disease", "level", "description"]
    list_per_page = 10
