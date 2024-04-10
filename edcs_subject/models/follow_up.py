from django.db import models

from edcs_constants.choices import POS_NEG, YES_NO, YES_NO_NA
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import FollowUpTest
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import FOLLOW_UP_TEST, PATIENT_STATUS_VISIT, QUALITY_OF_LIFE, SCALE
from ..model_mixins import CrfModelMixin


class FollowUp(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    sys_blood_pressure = models.IntegerField(
        verbose_name="Blood pressure: systolic",
        null=True,
        help_text="in mmHg",
    )

    dia_blood_pressure = models.IntegerField(
        verbose_name="Blood pressure: diastolic",
        null=True,
        help_text="in mmHg",
    )

    temperature = models.DecimalField(
        verbose_name="Temperature",
        decimal_places=1,
        max_digits=3,
        null=True,
        help_text="in °C",
    )

    respiratory_rate = models.IntegerField(
        verbose_name="Respiratory rate",
        null=True,
        help_text="in breaths/min",
    )

    pulse = models.IntegerField(
        verbose_name="Pulse",
        null=True,
        help_text="beats/min",
    )

    weight = models.DecimalField(
        verbose_name="Weight",
        decimal_places=1,
        max_digits=3,
        null=True,
        help_text="in Kg",
    )

    test_ordered = models.CharField(
        verbose_name="Have any test been ordered at this visit",
        choices=FOLLOW_UP_TEST,
        max_length=45,
        null=False,
        blank=True,
    )

    test_ordered_nw = models.ManyToManyField(
        FollowUpTest,
        verbose_name="Have any test been ordered at this visit",
    )

    test_ordered_other = edcs_models.OtherCharField()

    test_ordered_result = models.TextField(
        verbose_name="If yes, provide the results",
        null=True,
        blank=True,
        help_text="(Scan and upload all the results)",
    )

    hiv_status = models.CharField(
        verbose_name="What is the patient's HIV status?",
        max_length=45,
        choices=POS_NEG,
    )

    viral_load_cd4_off = models.IntegerField(
        verbose_name="If positive, was the blood sample for viral load and CD4 taken off?",
        null=True,
        blank=True,
    )

    current_viral_load = models.IntegerField(
        verbose_name="What is current Viral Load level",
        null=True,
        blank=True,
    )
    current_cd4_count = models.IntegerField(
        verbose_name="What is current CD4 count",
        null=True,
        blank=True,
    )

    hiv_genotype = models.CharField(
        verbose_name="Was the patient's HIV genotype done?",
        max_length=15,
        choices=YES_NO,
    )

    breathlessness_before = models.CharField(
        verbose_name="Has the patient had persistent breathlessness (Before)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    breathlessness_after = models.CharField(
        verbose_name="Has the patient had persistent breathlessness (After)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    tiredness_before = models.CharField(
        verbose_name="Has the patient had persistent tiredness or lack of energy (Before)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    tiredness_after = models.CharField(
        verbose_name="Has the patient had persistent tiredness or lack of energy (After)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    wheezing_before = models.CharField(
        verbose_name="Has the patient been wheezing (Before)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    wheezing_after = models.CharField(
        verbose_name="Has the patient been wheezing (After)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    shortness_breath_before = models.CharField(
        verbose_name="Has the patient had shortness of breath (Before)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    shortness_breath_after = models.CharField(
        verbose_name="Has the patient had shortness of breath (After)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    anorexia_before = models.CharField(
        verbose_name="Has the patient had anorexia (Before)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    anorexia_after = models.CharField(
        verbose_name="Has the patient had anorexia (After)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    cough_before = models.CharField(
        verbose_name="Has the patient had a cough that doesn't go away (Before)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    cough_after = models.CharField(
        verbose_name="Has the patient had a cough that doesn't go away (After)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    cough_get_worse_before = models.CharField(
        verbose_name="Has the patient had a long-standing cough that gets worse (Before)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    cough_get_worse_after = models.CharField(
        verbose_name="Has the patient had a long-standing cough that gets worse (After)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    coughing_blood_before = models.CharField(
        verbose_name="Has the patient been coughing up blood or rust-colored sputum "
        "(spit or phlegm) (Before)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    coughing_blood_after = models.CharField(
        verbose_name="Has the patient been coughing up blood or rust-colored sputum "
        "(spit or phlegm) (After)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    chest_infections_before = models.CharField(
        verbose_name="Has the patient had chest infections that keep coming back such as "
        "bronchitis, pneumonia (Before)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    chest_infections_after = models.CharField(
        verbose_name="Has the patient had chest infections that keep coming back such as "
        "bronchitis, pneumonia (After)? ",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    chest_pain_before = models.CharField(
        verbose_name="Has the patient had chest pain that is often worsen when breathing "
        "or coughing (Before)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    chest_pain_after = models.CharField(
        verbose_name="Has the patient had chest pain that is often worsen when breathing "
        "or coughing (After)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    hospitalized_before = models.CharField(
        verbose_name="Is patient hospitalized (Before)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    hospitalized_after = models.CharField(
        verbose_name="Is patient hospitalized (After)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )
    # *******************************************************
    walk_before = models.CharField(
        verbose_name="Has the patient been able to walk on their own (Before)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    walk_after = models.CharField(
        verbose_name="Has the patient been able to walk on their own (After)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    daily_activities_before = models.CharField(
        verbose_name="Has the patient been able to do activities of daily living (Before)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    daily_activities_after = models.CharField(
        verbose_name="Has the patient been able to do activities of daily living (After)?",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    pain_assess_before = models.CharField(
        verbose_name="Has the patient had pain (assess on a scale of 1-10) (Before)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )

    pain_assess_after = models.CharField(
        verbose_name="Has the patient had pain (assess on a scale of 1-10) (After)",
        max_length=6,
        null=True,
        choices=YES_NO,
    )
    # ***************************************************************
    other_presenting_symptoms = models.TextField(
        verbose_name="Any other presenting symptoms please specify?",
        blank=True,
        null=True,
    )

    CT_scan_done = models.CharField(
        verbose_name="Has the CT scan been done?",
        max_length=6,
        null=True,
        choices=YES_NO,
        help_text="(after 6th cycle which is between 4-6 months, or after 4 "
        "cycles depending on age)",
    )

    CT_scan_results = models.CharField(
        verbose_name="If yes,Did you get a copy of the CT scan results and CD?",
        max_length=6,
        null=True,
        choices=YES_NO_NA,
    )

    CT_scan_no_results = models.TextField(
        verbose_name="If you did not get a copy of the CT scan results and CD, Specify the "
        "reasons why?",
        blank=True,
        null=True,
    )

    CBC_done = models.CharField(
        verbose_name="Has the patient done a CBC?",
        max_length=6,
        null=True,
        choices=YES_NO,
        help_text="(WBC count, platelets and HB)",
    )

    CBC_results = models.CharField(
        verbose_name="If yes,Did you get a copy of the CBC results?",
        max_length=6,
        null=True,
        choices=YES_NO_NA,
    )

    CBC_no_results = models.TextField(
        verbose_name="If you did not get a copy of the CBC results, Specify the reasons why?",
        blank=True,
        null=True,
    )

    liver_renal_test_done = models.CharField(
        verbose_name="Has the patient done Liver Function Tests, Renal function tests?",
        max_length=6,
        null=True,
        choices=YES_NO,
        help_text="(mainly to assess for toxicity)",
    )

    liver_renal_test_results = models.CharField(
        verbose_name="If yes,Did you get a copy of the Liver Function and Renal function "
        "tests results?",
        max_length=6,
        null=True,
        choices=YES_NO_NA,
    )

    liver_renal_test_no_results = models.TextField(
        verbose_name="If you did not get a copy of the Liver Function and Renal function "
        "tests results, Specify the reasons why?",
        blank=True,
        null=True,
    )

    patient_visit_status = models.CharField(
        verbose_name="What is the patient status at this visit?",
        max_length=45,
        choices=PATIENT_STATUS_VISIT,
    )

    respond_treatment = models.CharField(
        verbose_name="If the patient is not responding to treatment, has the patient's "
        "treatment changed?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    treatment_change = models.TextField(
        verbose_name="If yes specify",
        null=True,
        blank=True,
    )
    # ********************************** new variable ****************************************
    strenuous_activities = models.CharField(
        verbose_name="Do you have any trouble doing strenuous activities,like carrying a heavy shopping bag or a suitcase?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    long_walk = models.CharField(
        verbose_name="Do you have any trouble taking a long walk?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    short_walk = models.CharField(
        verbose_name="Do you have any trouble taking a short walk outside of the house?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    stay_bed_chair = models.CharField(
        verbose_name="Do you need to stay in bed or a chair during the day?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    need_help = models.CharField(
        verbose_name="Do you need help with eating, dressing, washing yourself or using the toilet?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    limited_daily_activities = models.CharField(
        verbose_name="Were you limited in doing either your work or other daily activities?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    limited_leisure_activities = models.CharField(
        verbose_name="Were you limited in pursuing your hobbies or other leisure time activities?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    short_breath = models.CharField(
        verbose_name="Were you short of breath?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    had_pain = models.CharField(
        verbose_name="Have you had pain?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    need_rest = models.CharField(
        verbose_name="Did you need to rest?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    trouble_sleeping = models.CharField(
        verbose_name="Have you had trouble sleeping?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    felt_weak = models.CharField(
        verbose_name="Have you felt weak?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    lacked_appetite = models.CharField(
        verbose_name="Have you lacked appetite?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    felt_nauseated = models.CharField(
        verbose_name="Have you felt nauseated?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    vomited = models.CharField(
        verbose_name="Have you vomited?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    constipated = models.CharField(
        verbose_name="Have you been constipated?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    diarrhea = models.CharField(
        verbose_name="Have you had diarrhea?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    tired = models.CharField(
        verbose_name="Were you tired?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    pain_interfere_activities = models.CharField(
        verbose_name="Did pain interfere with your daily activities?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    difficulty_concentrating = models.CharField(
        verbose_name="Have you had difficulty in concentrating on things, like reading a newspaper or watching television?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    feel_tense = models.CharField(
        verbose_name="Did you feel tense?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    worry = models.CharField(
        verbose_name="Did you worry",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    feel_irritable = models.CharField(
        verbose_name="Did you feel irritable?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    depressed = models.CharField(
        verbose_name="Did you feel depressed",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    difficulty_remembering = models.CharField(
        verbose_name="Have you had difficulty remembering things?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    condition_interfered_family = models.CharField(
        verbose_name="Has your physical condition or medical treatment interfered with your family life?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    condition_interfered_social = models.CharField(
        verbose_name="Has your physical condition or medical treatment interfered with your social activities?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )
    condition_interfered_financial = models.CharField(
        verbose_name="Has your physical condition or medical treatment caused you financial difficulties?",
        max_length=15,
        null=True,
        choices=QUALITY_OF_LIFE,
    )

    rate_overall_health = models.CharField(
        verbose_name="How would you rate your overall health during the past week?",
        max_length=15,
        choices=SCALE,
        null=True,
        help_text="1 be very poor and 7 be excellent",
    )

    rate_overall_quality_life = models.CharField(
        verbose_name="How would you rate your overall quality of life during the past week?",
        max_length=15,
        choices=SCALE,
        null=True,
        help_text="1 be very poor and 7 be excellent",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Up"
