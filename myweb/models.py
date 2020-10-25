from django.db import models



class comment2(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f' - {self.name} - {self.text}'

