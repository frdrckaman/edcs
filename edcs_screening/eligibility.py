from django.utils.safestring import mark_safe
from edcs_constants.constants import NO, TBD, YES
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

    if obj.tb_diagnosis == YES or obj.malignancy == YES or obj.diagnosed_lung_cancer == YES:
        obj.eligible = False
        # reasons_ineligible.append("Subject unsuitable")
    else:
        obj.eligible = True if calculate_eligible_final(obj) == YES else False

    if obj.eligible:
        obj.reasons_ineligible = None
    else:
        if obj.tb_diagnosis == YES:
            reasons_ineligible.append("Patient have a positive TB diagnosis")
        if obj.malignancy == YES:
            reasons_ineligible.append("Patient had malignancy")
        if obj.diagnosed_lung_cancer == YES:
            reasons_ineligible.append("Patient diagnosed with lung cancer")
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
            obj.abnormal_chest_xrays == YES
            and obj.non_resolving_infection == YES
            and obj.lung_cancer_suspect == YES
            and obj.cough == YES
            and obj.long_standing_cough == YES
            and obj.cough_blood == YES
            and obj.chest_infections == YES
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
        display_label = "not eligible"
    return display_label
