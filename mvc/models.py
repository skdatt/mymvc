from django.db import models

class Student(models.Model):
    # Id=models.IntegerField()
    name = models.CharField(max_length=30)
    class Meta:
        db_table = "STUDENT_RECORD"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

#name,fees,age,email,dept
