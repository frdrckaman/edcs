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


class SmokingTobaccoProducts(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Smoking Tobacco Products"
        verbose_name_plural = "Smoking Tobacco Products"


class TobaccoProducts(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Tobacco Products"
        verbose_name_plural = "Tobacco Products"


class Contraceptives(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Contraceptives"
        verbose_name_plural = "Contraceptives"


class CovidVaccine(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Covid Vaccine"
        verbose_name_plural = "Covid Vaccine"


class HIVSubtype(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "HIV Subtype"
        verbose_name_plural = "HIV Subtype"


class SomaticMutations(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Somatic Mutations"
        verbose_name_plural = "Somatic Mutations"


class CookingDone(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Cooking Done"
        verbose_name_plural = "Cooking Done"


class CookingFuel(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Cooking Fuel"
        verbose_name_plural = "Cooking Fuel"


class CookingArea(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Cooking Area"
        verbose_name_plural = "Cooking Area"


class AirMonitorProblem(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Air Monitor Problem"
        verbose_name_plural = "Air Monitor Problem"


class OtherCookingFuel(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Other Cooking Fuel"
        verbose_name_plural = "Other Cooking Fuel"


class SolidFuel(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Solid Fuel"
        verbose_name_plural = "Solid Fuel"


class SolidFuelNew(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Solid Fuel New"
        verbose_name_plural = "Solid Fuel New"


class CancerInvestigation(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Cancer Investigation"
        verbose_name_plural = "Cancer Investigation"


class Industries(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Industries"
        verbose_name_plural = "Industries"


class FollowUpTest(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Follow up Test"
        verbose_name_plural = "Follow up Test"
