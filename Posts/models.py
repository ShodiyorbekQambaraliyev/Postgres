from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()

    def __str__(self):
        return self.ism