import re
from django.core.exceptions import ValidationError

def validate_subject_name(subject_name):
    regex = r"^[A-Z]+ /s[a-z]+$"
    good_name=re.match(regex, subject_name)
    if good_name:
        return subject_name
    
    raise ValidationError("Subject must be in title case format.")

def validate_professor(professor):
    regex = r"Professor + /s[A-Z][a-z]+$"
    good_name=re.match(regex, professor)
    if good_name:
        return professor
    
    raise ValidationError("Professor name must be in the format 'Professor Adam'.")