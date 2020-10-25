from django.db import models


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    Number = models.CharField(max_length=200)

    def __str__(self):
        return f' - {self.choice_text} - {self.Number}'

class comment2(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f' - {self.name} - {self.text}'

class Lecturer(models.Model):

    name = models.CharField(max_length=300, default='ดร.วิชิต สมบัติ')
    room = models.CharField(max_length=20, default='SC204')
    extension = models.CharField(max_length=20, default='4446')

    def __str__(self):
        return f'{self._id} {self.name}'
