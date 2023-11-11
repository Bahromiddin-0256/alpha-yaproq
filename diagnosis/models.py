from django.db import models

from common.models import BaseModel
from diagnosis.processing import process_image


class Diagnosis(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, related_name="diagnosis")
    image = models.ImageField(upload_to="diagnosis/")
    result = models.CharField(max_length=100, blank=True, null=True)
    percent = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def predict_disease(self):
        result, percent = process_image(self.image.path)
        self.result = result
        return result


class Disease(BaseModel):
    class DiseaseNameType(models.TextChoices):
        yellow_rust = "yellow_rust", "Yellow Rust"
        black_rust = "black_rust", "Black Rust"
        brown_rust = "brown_rust", "Brown Rust"
        septoria = "septoria", "Septoria"
        powdery_mildew = "powdery_mildew", "Powdery Mildew"

    name = models.CharField(max_length=100, choices=DiseaseNameType.choices, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class DiseaseLevel(BaseModel):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name="levels")
    level = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    percent = models.FloatField(default=0)

    def __str__(self):
        return self.level
