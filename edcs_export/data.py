import os
import shutil
from pathlib import Path

import environ
import pandas as pd
import sqlalchemy as db
from sqlalchemy import text

DATA_MODEL = [
    "django_site",
    "edcs_appointment_appointment",
    "edcs_consent_subjectconsent",
    "edcs_crf_crfstatus",
    "edcs_dashboard_dashboard",
    "edcs_device_device",
    "edcs_facility_holiday",
    "edcs_identifier_identifiermodel",
    "edcs_lists_airmonitorproblem",
    "edcs_lists_cancerinvestigation",
    "edcs_lists_contraceptives",
    "edcs_lists_cookingarea",
    "edcs_lists_cookingdone",
    "edcs_lists_cookingfuel",
    "edcs_lists_covidsymptoms",
    "edcs_lists_covidvaccine",
    "edcs_lists_familymembers",
    "edcs_lists_followuptest",
    "edcs_lists_hivsubtype",
    "edcs_lists_industries",
    "edcs_lists_lungcancersymptoms",
    "edcs_lists_othercookingfuel",
    "edcs_lists_smokingtobaccoproducts",
    "edcs_lists_solidfuel",
    "edcs_lists_somaticmutations",
    "edcs_lists_tobaccoproducts",
    "edcs_notification_notification",
    "edcs_registration_registeredsubject",
    "edcs_screening_subjectscreening",
    "edcs_sites_siteprofile",
    "edcs_subject_airpollutionfollowup",
    "edcs_subject_alcoholtobaccouse",
    "edcs_subject_alcoholtobaccouse_smoke_chew_tobacco",
    "edcs_subject_alcoholtobaccouse_tobacco_products",
    "edcs_subject_cancerhistory",
    "edcs_subject_cancerhistory_breast_cancer_family_member",
    "edcs_subject_cancerhistory_colon_cancer_family_member",
    "edcs_subject_cancerhistory_lung_cancer_family_member",
    "edcs_subject_cancerhistory_ovarian_cancer_family_member",
    "edcs_subject_cancerhistory_prostate_cancer_family_member",
    "edcs_subject_cancerhistory_thyroid_cancer_family_member",
    "edcs_subject_cancerhistory_uterine_cancer_family_member",
    "edcs_subject_clinicalreview",
    "edcs_subject_contraceptiveusereproductivehistory",
    "edcs_subject_contraceptiveusereproductivehistory_contraceptives",
    "edcs_subject_cookingfuel",
    "edcs_subject_covidinfectionhistory",
    "edcs_subject_covidinfectionhistory_covid_symptoms",
    "edcs_subject_covidinfectionhistory_covid_vaccine",
    "edcs_subject_deathreport",
    "edcs_subject_demographiccharacteristic",
    "edcs_subject_effectairpollution",
    "edcs_subject_followup",
    "edcs_subject_followup_test_ordered_nw",
    "edcs_subject_hivlabinvestigation",
    "edcs_subject_homelocator",
    "edcs_subject_housekitchensurrounding",
    "edcs_subject_labparta",
    "edcs_subject_labpartb",
    "edcs_subject_labpartc",
    "edcs_subject_labpartd",
    "edcs_subject_labpartd_hiv_subtype",
    "edcs_subject_labpartd_somatic_mutations",
    "edcs_subject_lungcancerlabinvestigation",
    "edcs_subject_lungcancertreatment",
    "edcs_subject_occupationalhistory",
    "edcs_subject_occupationalhistory_industries_worked",
    "edcs_subject_postairquality",
    "edcs_subject_postairquality_air_monitor_problem_list",
    "edcs_subject_postairquality_other_cooking_fuel",
    "edcs_subject_postairquality_solid_fuel",
    "edcs_subject_preairquality",
    "edcs_subject_preairquality_cooking_area",
    "edcs_subject_preairquality_cooking_done",
    "edcs_subject_signsymptomlungcancer",
    "edcs_subject_signsymptomlungcancer_investigations_ordered_nw",
    "edcs_subject_signsymptomlungcancer_what_brought_hospital",
    "edcs_subject_socioeconomiccharacteristic",
    "edcs_subject_subjectvisit",
    "edcs_visit_schedule_subjectschedulehistory",
    "edcs_visit_schedule_visitschedule",
    "multisite_alias",
]

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
)

environ.Env.read_env(ENV_DIR)

DB_DT_URL = env.str("DB_DT_URL")
EDCS_DATA_DIR = env.str("EDCS_DATA_DIR")

MYSQL_CONN = DB_DT_URL
engine = db.create_engine(MYSQL_CONN).connect()


def get_table_data(data):
    myQuery = text(f"select * from {data}")
    df = pd.read_sql_query(myQuery, engine)
    df.to_excel(f"{EDCS_DATA_DIR}/{data}.xlsx")
    return df


for data in DATA_MODEL:
    get_table_data(data)

shutil.make_archive(EDCS_DATA_DIR, "zip", EDCS_DATA_DIR)
