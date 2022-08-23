from django.db import models

# Create your models here.
class Students(models.Model):
    Name = models.CharField(max_length=30)
    Class = models.IntegerField()

    class Meta:
        db_table = "Student_info"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)