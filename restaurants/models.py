from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(null=True, blank=True)
    # null is where the 'NUMBER' should be zero or "ObJECT"; while blank = true is to pass if there is no input
