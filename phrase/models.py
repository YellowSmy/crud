from django.db import models

# Create your models here.
class Phrase(models.Model):
    id = models.AutoField(primary_key=True)
    phrase = models.CharField(max_length=30)

