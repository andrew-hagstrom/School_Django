from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from student_app.models import Student

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length = 255)
    professor = models.CharField(max_length = 255)
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self):
        return f"{self.subject_name} | {self.professor} | {self.students}"

    def add_a_student(self, id):
        # self.students=id
        self.students.add(id)
        print(self.students)
        if self.students.count() < 31 and id not in self.students: 
        # if count(self.students) < 31 and id not in self.students: 
            self.students.id = id 
        else:
            raise ValidationError("This subject is full!")
        

    def drop_a_student(self, id):
        if self.students.count() > 1 and id in self.students:
            self.students.remove(id)
        else:
            raise ValidationError("This subject is empty!")
