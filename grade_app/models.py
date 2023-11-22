from django.db import models

class Grade(models.Model):
    grade = models.DecimalField()
    a_subject = models.CharField(max_length = 255)
    student = models.ManyToManyField(Student, related_name='subjects')
