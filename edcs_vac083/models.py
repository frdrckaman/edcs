from django.db import models
from edcs_model.models import BaseUuidModel
from edcs_constants.choices import GENDER


class Demographic(BaseUuidModel):
    subject_initials = models.CharField(max_length=3)
    subject_id = models.CharField(max_length=9)
    visit_date = models.DateField()

    visit_code_choices = [
        ('1', 'sc1'),
    ]
    visit_code = models.CharField(max_length=1, choices=visit_code_choices)
    gender_choices = GENDER
    gender = models.CharField(max_length=1, choices=gender_choices)
    race_choices = [
        ('1', 'Africa'),
        ('2', 'Others'),
    ]
    race = models.CharField(max_length=1, choices=race_choices)
    dob = models.DateField()
    years = models.IntegerField()
    months = models.IntegerField()
    residence_choices = [
        ('1', 'Bagamoyo town'),
        ('2', 'Nearby district'),
    ]
    residence = models.CharField(max_length=1, choices=residence_choices)
    phone = models.IntegerField()
    literate_choices = [
        ('1', 'Yes'),
        ('2', 'No'),
        ('3', 'N/A'),
    ]
    literate = models.CharField(max_length=1, choices=literate_choices)
    education_choices = [
        ('1', 'Primary'),
        ('2', 'Secondary'),
        ('3', 'College'),
        ('4', 'Non-Formal'),
        ('5', 'N/A'),
    ]
    education = models.CharField(max_length=1, choices=education_choices)
    address = models.TextField()
    coordinator_initials = models.CharField(max_length=3)
    coordinator_time = models.TimeField()
    reviewer_initials = models.CharField(max_length=3)
    reviewer_time = models.TimeField()

    def __str__(self):
        return self.subject_id

