from edcs_subject.forms_collection import FormsCollection

from .crf import Crf

enrollment_crf = FormsCollection(
    Crf(show_order=100, model="edcs_subject.clinicalreview"),
    Crf(show_order=110, model="edcs_subject.demographiccharacteristic"),
    Crf(show_order=120, model="edcs_subject.hivLabinvestigation", required=False),
    Crf(show_order=130, model="edcs_subject.signsymptomlungCancer", required=False),
    Crf(
        show_order=140, model="edcs_subject.lungcancerlabinvestigation", required=False
    ),
    Crf(show_order=143, model="edcs_subject.lungCancertreatment"),
    Crf(show_order=144, model="edcs_subject.cancerhistory"),
    Crf(show_order=145, model="edcs_subject.covidinfectionhistory", required=False),
    Crf(
        show_order=150,
        model="edcs_subject.contraceptiveusereproductivehistory",
        required=False,
    ),
    Crf(show_order=155, model="edcs_subject.occupationalhistory", required=False),
    Crf(show_order=160, model="edcs_subject.alcoholtobaccouse"),
    Crf(show_order=165, model="edcs_subject.cookingfuel"),
    Crf(show_order=170, model="edcs_subject.housekitchensurrounding"),
    Crf(show_order=172, model="edcs_subject.effectairpollution"),
    Crf(show_order=174, model="edcs_subject.airpollutionfollowup"),
    Crf(show_order=176, model="edcs_subject.homelocatorform"),
    name="Enrollment CRFs",
)
