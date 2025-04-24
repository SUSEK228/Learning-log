from django.db import models

# Create your models here.


class Zadanie(models.Model):
    tresc = models.CharField(max_length=200)
    zrobione = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{'[x]' if self.zrobione else '[ ]'} {self.tresc}"