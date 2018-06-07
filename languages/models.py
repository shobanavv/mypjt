from django.db import models

# create single model
class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)
