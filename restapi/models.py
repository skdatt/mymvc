from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=30)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Author = models.CharField(max_length=30)
    Publication = models.CharField(max_length=30)

    class Meta:
        db_table = "BOOK_MASTER"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)
