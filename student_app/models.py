from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email, validate_combination_format
from django.core.validators import MinValueValidator, MaxValueValidator
# from subject_app.models import Subject
from django.core.exceptions import ValidationError

class Student(models.Model):
    """Student model"""
    name = models.CharField(max_length=255, default="John Doe", validators=[validate_name])
    student_email = models.EmailField(max_length=50, blank=False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=50, blank=True, unique=True)
    locker_number = models.IntegerField(blank=True, unique=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=10, blank=True, null=False, validators=[validate_combination_format])
    good_student = models.BooleanField(default=False)
    # subjects = models.ManyToManyField(Subject, related_name = 'students')

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number} - {self.student.id}"

    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.locker_number.save()
    
    def student_status(self, new_value):
        self.good_student= new_value
        self.good_student.save()

    def set_name(self, new_name):
        self.name = new_name
        self.full_clean_save()
    
    def set_student_email(self, new_student_email):
        self.student_email = new_student_email
        self.full_clean_save()
    
    def set_locker_combination(self, new_locker_combination):
        self.locker_combination = new_locker_combination
        self.full_clean_save()
    
    def add_subject(self, subject_id):
        if 0 < len(self.subjects) < 8:
            self.subjects.id = subject_id #Check equality statement
        else:
            raise ValidationError("This students class schedule is full!")   
            
    def remove_subject(self, subject_id):
        if len(self.subjects) >= 1:
            self.subjects.remove(subject_id)
        else:
            raise ValidationError("This students class schedule is empty!")
    
    def full_clean_save(self):
        self.full_clean()
        self.save()

        