from edcs_subject.forms_collection import FormsCollection

from .crf import Crf

enrollment_crf = FormsCollection(
    Crf(show_order=100, model="edcs_subject.clinicalreview"),
    Crf(show_order=110, model="edcs_subject.demographiccharacteristic"),
    Crf(show_order=115, model="edcs_subject.socioeconomiccharacteristic"),
    Crf(show_order=116, model="edcs_subject.alcoholtobaccouse"),
    Crf(show_order=117, model="edcs_subject.cancerhistory"),
    Crf(
        show_order=118,
        model="edcs_subject.contraceptiveusereproductivehistory",
        required=False,
    ),
    Crf(show_order=119, model="edcs_subject.occupationalhistory", required=False),
    Crf(show_order=120, model="edcs_subject.covidinfectionhistory", required=False),
    Crf(show_order=121, model="edcs_subject.signsymptomlungCancer", required=False),
    Crf(show_order=122, model="edcs_subject.lungCancertreatment"),
    Crf(show_order=123, model="edcs_subject.cookingfuel"),
    Crf(show_order=124, model="edcs_subject.housekitchensurrounding"),
    Crf(show_order=125, model="edcs_subject.effectairpollution"),
    # Crf(show_order=126, model="edcs_subject.airpollutionfollowup"),
    Crf(show_order=127, model="edcs_subject.homelocator"),
    Crf(show_order=128, model="edcs_subject.LabPartA"),
    Crf(show_order=129, model="edcs_subject.LabPartB"),
    Crf(show_order=130, model="edcs_subject.LabPartC"),
    Crf(show_order=131, model="edcs_subject.LabPartD"),
    Crf(show_order=132, model="edcs_subject.PreAirQuality"),
    Crf(show_order=133, model="edcs_subject.PostAirQuality"),
    name="Enrollment CRFs",
)

followup_crf = FormsCollection(
    Crf(show_order=100, model="edcs_subject.followup"),
    Crf(show_order=105, model="edcs_subject.deathreport"),
    name="Follow Up CRFs",
)
