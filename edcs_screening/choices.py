from edcs_constants.constants import CANCER_FREE, OTHER_CANCER, LUNG_CANCER_SUSPECT

CLINIC = (
    ("lung_cancer", "Lung cancer clinic/institute"),
    ("pathology", "Pathology"),
    ("other_clinic", "Other ward/clinic other than cancer"),
)

PATIENT_CATEGORY = (
    (LUNG_CANCER_SUSPECT, "Lung cancer suspect"),
    (OTHER_CANCER, "Other cancers"),
    (CANCER_FREE, "Cancer free")
)
