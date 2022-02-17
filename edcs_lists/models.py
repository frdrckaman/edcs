from edcs_list_data.model_mixins import ListModelMixin


class CovidSymptoms(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Covid Symptoms"
        verbose_name_plural = "Covid Symptoms"


class FamilyMembers(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Family Members"
        verbose_name_plural = "Family Members"


class LungCancerSymptoms(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Lung Cancer Symptoms"
        verbose_name_plural = "Lung Cancer Symptoms"
