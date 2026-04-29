from django.db import models

class Book(models.Model):
    
    title=models.CharField(max_length=200)
    price=models.FloatField()
    author=models.CharField(max_length=200)
    coopies=models.CharField(max_length=200)
    availcoopies=models.CharField(max_length=100)


    def __str__(self):
        return self.title

