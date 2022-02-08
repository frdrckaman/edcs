from edcs_list_data.model_mixins import ListModelMixin


class CovidSymptoms(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Covid Symptoms"
        verbose_name_plural = "Covid Symptoms"
