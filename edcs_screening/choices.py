from edcs_constants.constants import (
    CANCER_FREE,
    LUNG_CANCER_SUSPECT,
    NOT_APPLICABLE,
    OTHER_CANCER,
)

CLINIC = (
    ("lung_cancer", "Lung cancer clinic/institute"),
    ("pathology", "Pathology"),
    ("other_clinic", "Other ward/clinic other than cancer"),
)

PATIENT_CATEGORY = (
    (LUNG_CANCER_SUSPECT, "Lung cancer suspect"),
    (OTHER_CANCER, "Other cancers"),
    (CANCER_FREE, "Cancer free"),
)

OTHER_CANCER_DX = (
    (NOT_APPLICABLE, "Not applicable"),
    ("cervical_cancer", "Cervical cancer"),
    ("kaposi_sarcoma", "Kaposi sarcoma"),
    ("non_hodgkins_lymphoma", "Non Hodgkin’s lymphoma"),
)
