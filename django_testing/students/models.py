from django.db import models


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_name = models.TextField()
    birth_date = models.DateField()


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    students = models.ForeignKey(
        Student, related_name='students_id', on_delete=models.CASCADE)
