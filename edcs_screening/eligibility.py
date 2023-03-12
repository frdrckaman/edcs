from django.utils.safestring import mark_safe

from edcs_constants.constants import (
    CANCER_FREE,
    LUNG_CANCER_SUSPECT,
    NO,
    OTHER_CANCER,
    TBD,
    YES,
)
from edcs_utils.date import get_utcnow


class SubjectScreeningEligibilityError(Exception):
    pass


class EligibilityPartOneError(Exception):
    pass


class EligibilityPartTwoError(Exception):
    pass


class EligibilityPartThreeError(Exception):
    pass


def check_eligible_final(obj):
    """Updates model instance fields `eligible` and `reasons_ineligible`."""
    reasons_ineligible = []

    # if (
    #     obj.tb_diagnosis == YES
    #     or obj.malignancy == YES
    #     or (obj.patient_category == OTHER_CANCER and obj.diagnosed_lung_cancer == YES)
    # ):
    #     obj.eligible = False
    #     # reasons_ineligible.append("Subject unsuitable")
    if obj.patient_category == LUNG_CANCER_SUSPECT and obj.malignancy == YES:
        obj.eligible = False
    elif obj.patient_category == CANCER_FREE and (
        obj.malignancy == YES
        or obj.lung_cancer_suspect == YES
        or obj.diagnosed_lung_cancer == YES
    ):
        obj.eligible = False
    elif obj.patient_category == OTHER_CANCER and (
        obj.diagnosed_lung_cancer == YES or obj.lung_cancer_suspect == YES
    ):
        obj.eligible = False
    else:
        obj.eligible = True if calculate_eligible_final(obj) == YES else False

    if obj.eligible:
        obj.reasons_ineligible = None
    else:
        if obj.tb_diagnosis == YES:
            reasons_ineligible.append("Patient have a positive TB diagnosis")
        if obj.malignancy == YES and (
            obj.patient_category == LUNG_CANCER_SUSPECT or obj.patient_category == CANCER_FREE
        ):
            reasons_ineligible.append("Patient had malignancy")
        if obj.diagnosed_lung_cancer == YES and (
            obj.patient_category == CANCER_FREE or obj.patient_category == OTHER_CANCER
        ):
            reasons_ineligible.append("Patient diagnosed with lung cancer")
        if obj.lung_cancer_suspect == YES and (
            obj.patient_category == CANCER_FREE or obj.patient_category == OTHER_CANCER
        ):
            reasons_ineligible.append(
                "Patient been suspected to have lung cancer on the "
                "basis of clinical presentation"
            )
        if reasons_ineligible:
            obj.reasons_ineligible = "|".join(reasons_ineligible)
        else:
            obj.reasons_ineligible = None
    obj.eligibility_datetime = get_utcnow()


def calculate_eligible_final(obj):
    """Returns YES, NO or TBD."""
    if (
        obj.abnormal_chest_xrays in [YES, NO]
        and obj.non_resolving_infection in [YES, NO]
        and obj.lung_cancer_suspect in [YES, NO]
        and obj.cough in [YES, NO]
        and obj.long_standing_cough in [YES, NO]
        and obj.cough_blood in [YES, NO]
        and obj.chest_infections in [YES, NO]
    ):
        eligible = (
            # obj.abnormal_chest_xrays == YES
            # or obj.non_resolving_infection == YES
            # or obj.lung_cancer_suspect == YES
            # or obj.cough == YES
            # or obj.long_standing_cough == YES
            # or obj.cough_blood == YES
            # or obj.chest_infections == YES
            obj.tb_diagnosis == NO
            and (obj.above_eighteen == YES or obj.screening_consent == YES)
        )
        return NO if not eligible else YES
    return TBD


def format_reasons_ineligible(*str_values):
    reasons = None
    str_values = [x for x in str_values if x is not None]
    if str_values:
        str_values = "".join(str_values)
        reasons = mark_safe(str_values.replace("|", "<BR>"))
    return reasons


def eligibility_display_label(obj):
    if obj.eligible:
        display_label = "ELIGIBLE"
    elif calculate_eligible_final == TBD:
        display_label = "PENDING"
    else:
        display_label = "Not eligible"
    return display_label
