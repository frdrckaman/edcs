# from django import forms
# from edc_constants.constants import NO, YES
# from edcs_form_validators import FormValidator, FormValidatorMixin
# from edc_screening.modelform_mixins import AlreadyConsentedFormMixin
#
# from ..models import SubjectScreening
#
#
# class SubjectScreeningFormValidator(FormValidator):
#     def clean(self):
#         if (
#             not self.cleaned_data.get("screening_consent")
#             or self.cleaned_data.get("screening_consent") != YES
#         ):
#             raise forms.ValidationError(
#                 {
#                     "screening_consent": (
#                         "You may NOT screen this subject without their verbal consent."
#                     )
#                 }
#             )
#         if (
#             self.cleaned_data.get("age_in_years")
#             and self.cleaned_data.get("age_in_years") < 18
#         ):
#             raise forms.ValidationError(
#                 {"age_in_years": "Participant must be at least 18 years old."}
#             )
#         self.required_if(
#             YES, field="unsuitable_for_study", field_required="reasons_unsuitable"
#         )
#
#         self.applicable_if(
#             YES, field="unsuitable_for_study", field_applicable="unsuitable_agreed"
#         )
#
#         if self.cleaned_data.get("unsuitable_agreed") == NO:
#             raise forms.ValidationError(
#                 {
#                     "unsuitable_agreed": (
#                         "The study coordinator MUST agree with your assessment. "
#                         "Please discuss before continuing."
#                     )
#                 }
#             )
#
#
# class SubjectScreeningForm(AlreadyConsentedFormMixin, FormValidatorMixin, forms.ModelForm):
#     form_validator_cls = SubjectScreeningFormValidator
#
#     def clean(self):
#         cleaned_data = super().clean()
#         return cleaned_data
#
#     class Meta:
#         model = SubjectScreening
#         fields = [
#             "screening_consent",
#             "selection_method",
#             "clinic_type",
#             "report_datetime",
#             "initials",
#             "gender",
#             "age_in_years",
#             "qualifying_condition",
#             "lives_nearby",
#             "requires_acute_care",
#             "unsuitable_for_study",
#             "reasons_unsuitable",
#             "unsuitable_agreed",
#         ]
