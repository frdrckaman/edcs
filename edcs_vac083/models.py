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


class ExclusionCriteria(BaseUuidModel):
    subject_initials = models.CharField(max_length=3)
    subject_id = models.CharField(max_length=9)
    visit_date = models.DateField()
    visit_code_choices = [
        ('1', 'sc1'),
    ]
    visit_code = models.CharField(max_length=1, choices=visit_code_choices)
    yes_no_choices = [
        ('1', 'Yes'),
        ('2', 'No'),
    ]
    yes_no_na_choices = [
        ('1', 'Yes'),
        ('2', 'No'),
        ('3', 'NA'),
    ]
    eligibility_choices = [
        ('1', 'Eligibility criteria not fulfilled'),
        ('2', 'Consent withdrawal / not willing to participate'),
        ('3', 'Migrated / moved from the study area'),
        ('4', 'Other (please specify):'),
    ]
    products = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Use of immunoglobulins or blood products'
                                          ' (e.g., blood transfusion) at any time in the past')

    vaccine14 = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Receipt of any vaccine in the 14 days preceding enrolment,'
                                          ' or planned receipt of any\
                                            other vaccine within 14 days following each vaccination')

    vaccine30 = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Receipt of an investigational product in the 30 days preceding '
                                          'enrolment, or planned receipt during the study period')
    concurrent = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Concurrent involvement in another clinical trial or planned involvement '
                                          'during the study period')
    interpretation = models.CharField(max_length=1, choices=yes_no_na_choices,
                                help_text='Prior receipt of an investigational vaccine likely to impact on '
                                          'interpretation of the trial data, as assessed by the Investigator')
    confirmed = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Any confirmed or suspected immunosuppressive or immunodeficient state,'
                                          'including HIV infection; asplenia; recurrent, severe infections and chronic'
                                          ' (more than 14 days immunosuppressant medication within the past 6 months'
                                          ' (inhaled and topical steroids are allowed).')
    allergic = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='History of allergic disease or reactions likely to be exacerbated by any'
                                          'component of the vaccine (e.g. egg products)')
    anaphylaxis = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Any history of anaphylaxis in reaction to vaccinations')
    pregnant = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Pregnancy, lactation or intention to become pregnant during the study')
    cancer = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='History of cancer (except basal cell carcinoma of the skin and cervical'
                                          'Carcinoma in situ).')
    psychiatric = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='History of serious psychiatric condition that may affect'
                                          ' participation in the Study.')
    chronic = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Any other serious chronic illness requiring hospital '
                                          'specialist supervision')
    injecting = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Suspected or known injecting drug abuse in the 5 years '
                                          'preceding enrolment')
    surface = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Seropositive for hepatitis B surface antigen (HBsAg) or '
                                          'hepatitis C (HCV IgG).')
    volunteers = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Volunteers unable to be closely followed for social, '
                                          'geographic or psychological reasons.')
    clinically = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Any clinically significant abnormal finding on biochemistry or'
                                          ' hematology blood tests,urinalysis or clinical examination. '
                                          'In the event of clinically significant abnormal test results, '
                                          'confirmatory repeat tests will be requested. Procedures for identifying '
                                          'laboratory values meeting exclusion criteria will be described in'
                                          ' a study specific SOP.')
    disease = models.CharField(max_length=1, choices=yes_no_na_choices,
                                help_text='Any other significant disease, disorder, or finding which may '
                                          'significantly increase the risk to the volunteer because of'
                                          ' participation in the study, affect the ability of the volunteer'
                                          ' to participate in the study or impair interpretation of the study data.')
    enrolled = models.CharField(max_length=1, choices=yes_no_choices,
                                help_text='Can the participant be enrolled in the study?')
    reason = models.CharField(max_length=1, choices=eligibility_choices,
                                help_text='*If No, specify the reason for screening failure (Tick one box only)')

    clinician_initials = models.CharField(max_length=3, help_text='Clinician Initials:')
    coordinator_time = models.TimeField()
    pi_initials = models.CharField(max_length=3, help_text='PI /designee')
    reviewer_time = models.TimeField()

    def __str__(self):
        return self.subject_id


class ScreeningTwo(BaseUuidModel):
    subject_initials = models.CharField(max_length=3)
    subject_id = models.CharField(max_length=9)
    yes_no_choices = [
        ('1', 'Yes'),
        ('2', 'No'),
    ]
    yes_no_na_choices = [
        ('1', 'Yes'),
        ('2', 'No'),
        ('3', 'NA'),
    ]
    visitOccur = models.CharField(max_length=1, choices=yes_no_choices)
    visit_code_choices = [
        ('1', 'sc2'),
    ]
    visit_date = models.DateField()
    visitYes_choices = [
        ('1', 'Subject illness or injury'),
        ('2', 'Subject refusal'),
        ('3', 'Scheduling difficulties'),
        ('4', 'Unable to contact'),
        ('5', 'Transportation problems'),
        ('6', 'Temporarily out of study area'),
        ('7', 'Subject forgot'),
        ('8', 'Site decision/error, specify:'),
        ('9', 'Other, specify:'),
    ]
    results = models.CharField(max_length=1, choices=yes_no_choices,
                               help_text='Did you inform the participant about their results?')
    health = models.CharField(max_length=1, choices=yes_no_choices,
                               help_text='Has there been change in participant’s health status since last visit?')
    medication = models.CharField(max_length=1, choices=yes_no_choices,
                               help_text='Is the participant currently taking new medications not previously noted?')
    sample = models.CharField(max_length=1, choices=yes_no_na_choices,
                               help_text='Were all requested sample collected?')
    sampleNumber = models.IntegerField(help_text='Sample Brady Number')
    coordinator_initials = models.CharField(max_length=3)
    coordinator_time = models.TimeField()
    reviewer_initials = models.CharField(max_length=3)
    reviewer_time = models.TimeField()

    def __str__(self):
        return self.subject_id


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title