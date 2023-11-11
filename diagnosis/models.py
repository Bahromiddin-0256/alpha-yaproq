from django.db import models

from common.models import BaseModel
from diagnosis.processing import process_image


class Diagnosis(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="diagnosis/")
    result = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def predict_disease(self):
        result = process_image(self.image.path)
        self.result = result
        return result
