from django.apps import apps as django_apps
from django.conf import settings
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
# from edcs_metadata.constants import KEYED, REQUIRED
from edcs_model_wrapper import ModelWrapper


class SubjectVisitModelWrapper(ModelWrapper):

    model = settings.SUBJECT_VISIT_MODEL
    cancel_url_attrs = ["subject_identifier"]
    cancel_url_name = "subject_dashboard_url"
    next_url_attrs = ["subject_identifier", "appointment"]
    next_url_name = "subject_dashboard_url"
    querystring_attrs = ["reason"]

    @property
    def appointment(self):
        return str(self.object.appointment.id)

    @property
    def appointment_model_cls(self):
        return self.object.appointment.__class__

    @property
    def subject_identifier(self):
        return self.object.subject_identifier

    @property
    def crf_metadata(self):
        CrfMetadata = django_apps.get_model("edc_metadata.crfmetadata")
        return CrfMetadata.objects.filter(
            subject_identifier=self.object.subject_identifier,
            visit_code=self.object.visit_code,
            visit_code_sequence=self.object.visit_code_sequence,
            entry_status__in=["KEYED", "REQUIRED"],
        )

    @property
    def requisition_metadata(self):
        RequisitionMetadata = django_apps.get_model("edc_metadata.requisitionmetadata")
        return RequisitionMetadata.objects.filter(
            subject_identifier=self.object.subject_identifier,
            visit_code=self.object.visit_code,
            visit_code_sequence=self.object.visit_code_sequence,
            entry_status__in=["KEYED", "REQUIRED"],
        )

    @property
    def subject_dashboard_href(self):
        """Returns a complete url + quertystring to return to the
        subject's dashboard.

        Used by `edc_review_dashboard`.
        """
        kwargs = dict(
            subject_identifier=self.object.subject_identifier,
            appointment=str(self.object.appointment.pk),
        )
        try:
            url = reverse(self.next_url, kwargs=kwargs)
        except NoReverseMatch as e:
            raise NoReverseMatch(
                f"{e}. Using url_name='{self.next_url}',"
                f"kwargs={kwargs}.  See {repr(self)}."
            )
        return url
