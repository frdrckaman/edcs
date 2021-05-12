from django.db import models
from edcs_model.models import BaseUuidModel
from edcs_constants.choices import GENDER
from django.db.models import F, Q, When


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
        ('O', 'Others'),
    ]
    race = models.CharField(max_length=1, choices=race_choices)
    race_other = models.TextField(verbose_name='Specify',default='',editable=True)
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

    class Media:
        js = ('edcs_vac083/js/condition_logic.js')


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
    products = models.CharField(verbose_name='Use of immunoglobulins or blood products', max_length=1,
                                choices=yes_no_choices,
                                help_text='(e.g., blood transfusion) at any time in the past')

    vaccine14 = models.CharField(verbose_name='Receipt of any vaccine in the 14 days preceding enrolment, or '
                                              'planned receipt of any\
                                               other vaccine within 14 days following each vaccination',
                                 max_length=1, choices=yes_no_choices
                                 )

    vaccine30 = models.CharField(verbose_name='Receipt of an investigational product in the 30 days preceding \
                                               enrolment, or planned receipt during the study period',
                                 max_length=1, choices=yes_no_choices
                                 )
    concurrent = models.CharField(max_length=1, choices=yes_no_choices,
                                  verbose_name='Concurrent involvement in another clinical trial or planned'
                                               ' involvement '
                                               'during the study period')
    interpretation = models.CharField(max_length=1, choices=yes_no_na_choices,
                                      verbose_name='Prior receipt of an investigational vaccine likely to impact on '
                                                   'interpretation of the trial data, as assessed by the Investigator')
    confirmed = models.CharField(max_length=1, choices=yes_no_choices,
                                 verbose_name='Any confirmed or suspected immunosuppressive or immunodeficient state,'
                                              'including HIV infection; asplenia; recurrent, severe infections '
                                              'and chronic'
                                              ' (more than 14 days immunosuppressant medication within the past '
                                              '6 months'
                                              ' (inhaled and topical steroids are allowed).')
    allergic = models.CharField(max_length=1, choices=yes_no_choices,
                                verbose_name='History of allergic disease or reactions likely to be exacerbated by any'
                                             'component of the vaccine (e.g. egg products)')
    anaphylaxis = models.CharField(max_length=1, choices=yes_no_choices,
                                   verbose_name='Any history of anaphylaxis in reaction to vaccinations')
    pregnant = models.CharField(max_length=1, choices=yes_no_choices,
                                verbose_name='Pregnancy, lactation or intention to become pregnant during the study')
    cancer = models.CharField(max_length=1, choices=yes_no_choices,
                              verbose_name='History of cancer (except basal cell carcinoma of the skin and cervical'
                                           'Carcinoma in situ).')
    psychiatric = models.CharField(max_length=1, choices=yes_no_choices,
                                   verbose_name='History of serious psychiatric condition that may affect'
                                                ' participation in the Study.')
    chronic = models.CharField(max_length=1, choices=yes_no_choices,
                               verbose_name='Any other serious chronic illness requiring hospital '
                                            'specialist supervision')
    injecting = models.CharField(max_length=1, choices=yes_no_choices,
                                 verbose_name='Suspected or known injecting drug abuse in the 5 years '
                                              'preceding enrolment')
    surface = models.CharField(max_length=1, choices=yes_no_choices,
                               verbose_name='Seropositive for hepatitis B surface antigen (HBsAg) or '
                                            'hepatitis C (HCV IgG).')
    volunteers = models.CharField(max_length=1, choices=yes_no_choices,
                                  verbose_name='Volunteers unable to be closely followed for social, '
                                               'geographic or psychological reasons.')
    clinically = models.CharField(max_length=1, choices=yes_no_choices,
                                  verbose_name='Any clinically significant abnormal finding on biochemistry or'
                                               ' hematology blood tests,urinalysis or clinical examination. '
                                               'In the event of clinically significant abnormal test results, '
                                               'confirmatory repeat tests will be requested. Procedures for '
                                               'identifying '
                                               'laboratory values meeting exclusion criteria will be described in'
                                               ' a study specific SOP.')
    disease = models.CharField(max_length=1, choices=yes_no_na_choices,
                               verbose_name='Any other significant disease, disorder, or finding which may '
                                            'significantly increase the risk to the volunteer because of'
                                            ' participation in the study, affect the ability of the volunteer'
                                            ' to participate in the study or impair interpretation of the study data.')
    enrolled = models.CharField(max_length=1, choices=yes_no_choices,
                                verbose_name='Can the participant be enrolled in the study?')
    reason = models.CharField(max_length=1, choices=eligibility_choices,
                              verbose_name='*If No, specify the reason for screening failure (Tick one box only)')

    clinician_initials = models.CharField(max_length=3, verbose_name='Clinician Initials:')
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
    visit_code = models.CharField(max_length=1, choices=visit_code_choices, default="", editable=True)
    visit_date = models.DateField()
    visitNo_choices = [
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
    reason = models.CharField(max_length=1, choices=visitNo_choices, default="", editable=True)
    site_decision = models.TextField(verbose_name='Site decision/error, specify:', default="", editable=True)
    reason_other = models.CharField(max_length=25, verbose_name='Other, specify:', default="", editable=True)
    results = models.CharField(max_length=1, choices=yes_no_choices,
                               verbose_name='Did you inform the participant about their results?')
    health = models.CharField(max_length=1, choices=yes_no_choices,
                              verbose_name='Has there been change in participant’s health status since last visit?')
    medication = models.CharField(max_length=1, choices=yes_no_choices,
                                  verbose_name='Is the participant currently taking new medications'
                                               ' not previously noted?')
    sample = models.CharField('Were all requested sample collected?', max_length=1, choices=yes_no_na_choices
                              )
    sampleNumber = models.IntegerField(verbose_name='Sample Brady Number')
    additional = models.CharField(max_length=20, verbose_name='Were additional OR repeat tests requested at this '
                                                              'visit?',
                                  choices=yes_no_na_choices, default="", editable=True
                                  )

    additional_test_choices = [('1', 'Hematology'),
                               ('2', 'Biochemistry'),
                               ('3', 'Parasitology'),
                               ('4', 'Urinalysis'),
                               ('5', 'Pregnancy Test'),
                               ('6', 'Serology'),
                               ('7', 'Other')
                               ]
    additional_test = models.CharField(max_length=1, verbose_name='If “yes’ specify which tests were '
                                                                   'requested below and '
                                                                   'complete unscheduled laboratory investigation '
                                                                   'form:',
                                       choices=additional_test_choices, default="", editable=True)

    additional_test_other = models.TextField(verbose_name='Specify', default="", editable=True)

    procedures = models.CharField(max_length=1, verbose_name='Did all procedures of SC2 been completed?',
                                  choices=yes_no_choices, default="", editable=True)

    procedures_no_choices = [('1', 'Volunteer requires treatment before enrolment (update medical history section)'),
                             ('2', 'Volunteer require repeat/additional sample analysis'),
                             ('3', 'Other, please specify'),
                             ]
    procedures_no = models.CharField(max_length=25, verbose_name='If No, Tick appropriate reason.',
                                     choices=procedures_no_choices, default="", editable=True)

    procedures_no_other = models.CharField(max_length=25, verbose_name='If No, Specify', default="", editable=True)

    referral = models.CharField(max_length=1, verbose_name='Does volunteer require referral to another '
                                                           'health facility '
                                                           'for further medical care?', choices=yes_no_choices,
                                default="", editable=True)

    referral_yes = models.TextField(verbose_name='If Yes, specify below and complete appropriate referral '
                                                 'document', choices=yes_no_choices, default="", editable=True)

    bednet = models.CharField(max_length=20, verbose_name='Did the volunteer receive an insecticide treated bed net?',
                              choices=yes_no_choices, default="", editable=True)

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

