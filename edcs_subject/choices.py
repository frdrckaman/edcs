from edcs_constants.constants import (
    ASTHMA,
    COPD,
    DECLINE_TO_ANSWER,
    DONT_KNOW,
    GREATER_THAN_6MONTHS,
    INTERSTITIAL_LUNG_DISEASE,
    LEFT,
    NEG,
    NEGATIVE,
    NEGATIVE_TEST,
    NEVER,
    NO,
    NONE,
    NONE_OF_ABOVE,
    NOT_APPLICABLE,
    NOT_DONE,
    OTHER,
    POSITIVE,
    POSITIVE_TEST,
    RIGHT,
    UNKNOWN,
    YES_CURRENT_CHEW,
    YES_CURRENT_CONSUMER,
    YES_CURRENT_SMOKER,
    YES_CURRENT_USER,
    YES_PAST_CHEW,
    YES_PAST_CONSUMER,
    YES_PAST_SMOKER,
    YES_PAST_USER,
)
from edcs_subject.constants import (
    HOSPITAL_CLINIC,
    MISSED_VISIT,
    NOT_RESPOND_TREATMENT,
    POS_CK5_6,
    POS_CK7,
    POS_CK20,
    POS_P40,
    POS_P63,
    POS_PANCYTOKERATINE,
    POS_TTF1,
    SCHEDULED,
    UNSCHEDULED,
)

from .constants import NON_SMALL_CELL

MISS_ARV = (
    ("at_least_once_every_week", "At least once every week"),
    ("at_least_once_a_month", "At least once in a month"),
    ("at_least_once_3_months", "At least once in 3 months"),
    ("at_least_once_a_year", "At least once a year"),
    ("dont_remember", "I Do not remember"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

LUNG_DISEASE = (
    (COPD, "Yes, COPD"),
    (ASTHMA, "Yes, Asthma"),
    (INTERSTITIAL_LUNG_DISEASE, "Yes, Interstitial Lung Disease"),
    (NO, "No"),
    ("decline_to_answer", "Decline to answer"),
    (DONT_KNOW, "Do not know"),
)
EDUCATION = (
    ("never_been_in_school", "Never been in school"),
    ("primary_education", "Completed Primary Education"),
    ("secondary_education", "Completed Secondary Education (‘’O’’ or ‘’A’’ level)"),
    ("vocational_training", "Vocational training"),
    ("tertiary_education", "Tertiary Education"),
    (OTHER, "Other"),
)

OCCUPATION = (
    ("civil_servant", "Civil Servant"),
    ("house_wife", "House wife"),
    ("peasant", "Peasant"),
    ("petty_trader", "Petty trader"),
    ("entrepreneur", "Entrepreneur"),
    ("unemployed", "Unemployed"),
    ("business_man", "Business man/woman"),
    ("casual_laborers", "Casual laborers"),
    (OTHER, "Other"),
)

MATERIAL_BUILD_FLOOR = (
    ("soil_sand_mud", "Soil/ sand/ mud"),
    ("cement_concrete_tiles", "Cement/ concrete/ tiles"),
    (OTHER, "Others"),
)

IRON = (
    ("yes_electrical", "Yes electrical"),
    ("yes_charcoal_iron", "Yes charcoal iron"),
    ("no", "No"),
)

MATERIAL_BUILD_WALL = (
    ("soil_sand_mud", "There is no wall"),
    ("cement_concrete_tiles", "Grass"),
    ("canes_palms", "Canes/ Palm"),
    ("trees_mud", "Trees and mud"),
    ("stone_mud", "Stones and mud"),
    ("wood_timber", "Wood/timber"),
    ("cement_concrete_bricks", "Cement/ concrete blocks/ burnt blocks/bricks."),
    (OTHER, "Others"),
)

MATERIAL_BUILD_ROOFING = (
    ("soil_sand_mud", "Iron sheet/roofing tiles"),
    ("grass_leaves_soil", "Grass/ leaves/ palm leaves/ soil"),
    (OTHER, "Others"),
)

COOKING = (
    ("electricity_stove", "Electricity stove"),
    ("gas_stove", "Gas stove"),
    ("kerosene_stove", "Kerosene stove"),
    ("charcoal", "Charcoal"),
    ("logs_woods", "Logs/woods"),
    ("grass_leaves", "Grass/leaves"),
    ("animal_waste", "Animal waste"),
    ("plants_waste", "Plants waste"),
    ("dont_cook", "We do not cook"),
    (OTHER, "Others"),
)

POWER_SOURCE = (
    ("electricity", "Electricity"),
    ("battery_torch", "Battery/ torch "),
    ("solar_energy", "Solar energy"),
    ("kerosene", "Kerosene"),
    (OTHER, "Others"),
)

SMOKE_TOBACCO_PRODUCTS = (
    (YES_CURRENT_SMOKER, "Yes, Current smoker"),
    (YES_PAST_SMOKER, "Yes, past smoker"),
    (YES_CURRENT_CHEW, "Yes, current chew tobacco"),
    (YES_PAST_CHEW, "Yes, past chew tobacco"),
    (NEVER, "Never"),
)

TOBACCO_PRODUCTS = (
    ("yes_cigarettes", "Yes, Cigarettes"),
    ("yes_cigars", "Yes, Cigars"),
    ("yes_shisha", "Yes, Shisha"),
    ("yes_pipes", "Yes, pipes"),
    ("none_of_above", "None of the above"),
    (NOT_APPLICABLE, "Not applicable"),
)

SMOKE_TOBACCO_PRODUCTS_FREQUENCY = (
    ("daily", "Daily"),
    ("every_other_day", "Every other day"),
    ("weekly", "Weekly (Not daily)"),
    ("monthly", "Monthly(Not weekly)"),
    (OTHER, "Others"),
    (NOT_APPLICABLE, "Not applicable"),
)

SMOKE_INSIDE = (
    ("daily", "Daily"),
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
    ("less_than_monthly", "Less than monthly"),
    ("never", "Never"),
    (OTHER, "Others"),
    (NOT_APPLICABLE, "Not applicable"),
)

ALCOHOL_CONSUMPTION = (
    (YES_CURRENT_CONSUMER, "Yes, Current consumer"),
    (YES_PAST_CONSUMER, "Yes, past consumer"),
    (NEVER, "Never"),
)

ALCOHOL_CONSUMPTION_FREQUENCY = (
    ("daily", "1-Daily"),
    ("every_other_day", "Every other day"),
    ("weekly", "Weekly (Not daily )"),
    ("monthly", "Monthly (Not weekly)"),
    (OTHER, "Others"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN60 = (
    ("less_than_12yrs", "≤ 12 years"),
    ("12_13yrs", "12-13 years"),
    ("14_15yrs", "14-15 years"),
    ("greater_than_16yrs", "≥ 16 years"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN61 = (
    ("nulliparous", "Nulliparous"),
    ("less_than_20yrs", "≤ 20years"),
    ("20_29yrs", "20-29 years"),
    ("30_39yrs", "30-39 years"),
    ("greater_than_39yrs", "≥ 39 years"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN62 = (
    ("nulliparous", "Nulliparous"),
    ("less_than_25yrs", "≤ 25years"),
    ("25_29_yrs", "25-29 years"),
    ("30_39yrs", "30-39 years"),
    ("greater_than_39yrs", "≥ 39 years"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN64 = (
    (YES_CURRENT_USER, "Yes, Current user"),
    (YES_PAST_USER, "Yes, Past user"),
    (NO, "No"),
    (DECLINE_TO_ANSWER, "Decline to answer"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN65 = (
    ("less_than_5yrs", "≤ 5 years"),
    ("greater_than_5yrs", "≥ 5 years"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN66 = (
    ("less_than_5yrs_ago", "≤ 5 years ago"),
    ("greater_than_5yrs_ago", "≥ 5 years ago"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN70 = (
    ("less_than_46yrs", "≤ 46 years"),
    ("46_50yrs", "46-50 years"),
    ("greater_than_51yrs", "≥ 51 years"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN72 = (
    ("textile_industry", "Textile industry"),
    ("chemical_production_industry", "Chemical production industry"),
    ("food_processing_industry", "Food processing industry"),
    ("drug_industry", "Drug industry"),
    ("milling_industry", "Milling industry"),
    ("construction_industry", "Construction industry"),
    ("gas_fuel_stations", "Gas / fuel stations"),
    ("cement_industry", "Cement industry"),
    (NOT_APPLICABLE, "Not applicable"),
    (OTHER, "Other"),
)

COVID_SYMPTOMS = (
    ("headache", "Headache"),
    ("fever", "Fever"),
    ("muscle_ache", "Muscle ache"),
    ("weakness_tiredness", "Weakness/tiredness "),
    ("nausea_vomiting", "Nausea/vomiting"),
    ("abdominal_pain", "Abdominal pain"),
    ("diarrhea", "Diarrhea"),
    ("sore_throat", "Sore throat"),
    ("cough", "Cough"),
    ("shortness_of_breath", "Shortness of breath"),
    ("loss_taste", "Loss of taste"),
    ("no_loss_smell", "No Loss of smell"),
)

QN82 = (
    (POSITIVE_TEST, "One or more positive test(s) "),
    (NEGATIVE_TEST, "One or more negative tests, but none were positive"),
    ("all_test_failed", "All tests failed"),
    ("waiting_results", "Waiting for all results"),
    (NOT_APPLICABLE, "Not applicable"),
)

COVID_VACCINE = (
    (NOT_APPLICABLE, "Not applicable"),
    ("dont_know_type", "Don’t know type"),
    ("pfizer_biontech_moderna", "Pfizer/BioNTech Moderna"),
    ("oxford_astraZeneca", "Oxford/AstraZeneca"),
    ("janssen_johnson_Johnson", "Janssen\Johnson&Johnson"),
    ("novavax", "Novavax"),
    ("sinovac", "Sinovac"),
    ("sputnik", "Sputnik"),
    ("valneva", "Valneva"),
    ("sinopharm", "Sinopharm"),
    (OTHER, "Other"),
)

QN87 = (
    ("government_tz_ug", "Government of Tanzania/Uganda"),
    ("research_study", "Research study/trial "),
    (OTHER, "Others"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN88 = (
    ("one", "One"),
    ("two", "Two"),
    ("three_more", "Three or More"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN90 = (
    ("cough_dont_go_away", "A cough that doesn't go away after 2 or 3 weeks"),
    ("long_standing_cough", "A long-standing cough that gets worse"),
    ("coughing_blood", "Coughing up blood or rust-colored sputum (spit or phlegm)"),
    (
        "chest_infections",
        "Chest infections that keep coming back such as bronchitis, pneumonia etc",
    ),
    ("chest_pain", "Chest pain that is often worsen when breathing or coughing"),
    ("persistent_breathlessness", "Persistent breathlessness"),
    ("persistent_tiredness", "Persistent tiredness or lack of energy"),
    ("wheezing", "Wheezing"),
    ("shortness_of_breath", "Shortness of breath"),
    ("unexplained_weight_loss", "Unexplained weight loss"),
    (OTHER, "Others"),
)

QN91 = (
    ("less_than_1month", "Less than 1 month"),
    ("1_3months", "1-3 months"),
    ("3_6months", "3-6 months"),
    (GREATER_THAN_6MONTHS, ">6 months"),
)

QN92 = (
    ("sudden_onset", "Sudden onset"),
    ("gradual_onset", "Gradual onset"),
    ("progressive_severity", "Progressive in severity"),
    ("intermittent_severity", "Intermittent in severity"),
    (OTHER, "Others"),
)

QN94 = (
    ("mother", "Mother"),
    ("father", "Father"),
    ("brother", "Brother"),
    ("sister", "Sister"),
    ("grandparent_mother_side", "Grandparent from mother’s side"),
    ("grandparent_father_side", "Grandparent from father’s side"),
    (NOT_APPLICABLE, "Not applicable"),
    (OTHER, "Others"),
)

QN95 = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("family_history_unknown", "Family history unknown"),
)

QN98 = (
    ("blood_tests", "Blood tests"),
    ("chest_xray", "Chest X-ray"),
    ("ct_scan", "CT scan"),
    ("lung_cancer_biopsy", "Lung cancer biopsy"),
    ("sputum_tb_dx", "Sputum for TB diagnosis"),
    (OTHER, "Others"),
    (NONE_OF_ABOVE, "None of the above"),
)

QN100 = (
    ("yes", "Yes"),
    ("no_declined", "No, declined"),
    ("no_sputum", "No sputum"),
)

QN101 = (
    ("TB_POS", "TB positive"),
    ("TB_NEG", "TB negative (No TB)"),
    ("inconclusive_results", "Inconclusive results"),
)

QN102 = (
    ("lung_cancer_confirmed", "Lung cancer confirmed"),
    ("non_cancerous", "Non-cancerous"),
    ("inconclusive_results", "Inconclusive results"),
)

QN103 = (
    ("one", "One (1)"),
    ("two", "Two (2)"),
    ("three", "Three (3)"),
    ("four", "Four (4)"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN105 = (
    ("chemotherapy", "Chemotherapy"),
    ("radiation", "Radiation"),
    ("surgical_resection", "Surgical resection"),
    ("immunotherapy", "Immunotherapy"),
    ("tyrosine_kinase_inhibitor", "Tyrosine kinase inhibitor "),
    ("1_2above", "1 & 2 above"),
    (OTHER, "Others"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN106 = (
    ("HIV_POS", "HIV positive"),
    ("HIV_NEG", "HIV negative"),
    ("inconclusive_results", "Inconclusive results"),
)

QN110 = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN1AP = (
    ("electricity", "Electricity"),
    ("lpg_natural_gas ", "LPG/Natural gas "),
    ("biogas ", "Biogas "),
    ("kerosene", "Kerosene"),
    ("coal_lignite", "Coal/lignite"),
    ("charcoal", "Charcoal"),
    ("wood", "Wood"),
    ("straw_shrubs_grass ", "Straw/shrubs/grass "),
    ("agricultural_crop", "Agricultural crop"),
    ("animal_dung", "Animal dung"),
    (OTHER, "Other"),
    ("no_food_cooked", "No food cooked in household"),
)

QN2AP = (
    ("Economical", "Economical"),
    ("Convenient", "Convenient"),
    ("easily_available", "Easily available"),
    ("good_health", "Good for health"),
    ("looks_better", "Looks better"),
)

QN3AP = (
    ("in_house", "In the house"),
    ("separate_building", "In a separate building"),
    ("outdoors", "Outdoors"),
    (OTHER, "Other"),
)

QN5AP = (
    ("yes_all_times", "Yes, all the times"),
    ("yes_sometimes", "Yes, sometimes"),
    ("no", "No"),
)

QN7AP = (
    ("25_days_month", "At least 25% of the days in a month"),
    ("25_50_days_month", "25%-50% of the days in a month"),
    ("50_70_days_month", "50-75% of the days in a month"),
    ("75_100_days_month", "75%-100% of the days in a month"),
    (NOT_APPLICABLE, "Not applicable"),
)
QN28AP = (
    ("electricity", "Electricity"),
    ("lpg_natural_gas ", "LPG/Natural gas "),
    ("biogas ", "Biogas "),
    ("kerosene", "Kerosene"),
    ("coal_lignite", "Coal/lignite"),
    ("charcoal", "Charcoal"),
    ("wood", "Wood"),
    ("straw_shrubs_grass ", "Straw/shrubs/grass "),
    ("agricultural_crop", "Agricultural crop"),
    ("animal_dung", "Animal dung"),
    (OTHER, "Other"),
    ("dont_know", "I dont know"),
)

QN30AP = (
    ("earth_sand_clay_mud_dung", "Earth/sand/clay/mud/dung"),
    ("wood", "Wood"),
    ("ceramic_tiles_vinyl", "Ceramic tiles or vinyl"),
    ("cement_concrete", "Cement/concrete"),
    (OTHER, "Other"),
)

QN31AP = (
    ("no_roof", "No roof"),
    ("thatch_straw", "Thatch/straw"),
    ("mud", "Mud"),
    ("metal", "Metal"),
    ("wood", "Wood"),
    ("brick", "Brick"),
    ("tiles", "Tiles"),
    ("slate", "Slate"),
    (OTHER, "Others"),
)

QN32AP = (
    ("no_walls", "No walls"),
    ("mud", "Mud"),
    ("bricks", "Bricks"),
    ("wood", "Wood"),
    ("cement_concrete", "Cement/concrete"),
    ("stone", "Stone"),
    ("metal", "Metal"),
    (OTHER, "Others"),
)

QN34AP = (
    ("daily", "Daily"),
    ("two_day_week", "Two days a week"),
    ("three_day_week", "Three days a week"),
    ("four", "Four"),
    ("five", "Five"),
    ("six", "Six"),
    ("weekly", "Weekly (i.e., once in 7 days)"),
    ("monthly", "Monthly"),
    ("less_one_month", "Less than once a month"),
    ("never", "Never"),
)

QN36AP = (
    ("no_roof", "No roof"),
    ("thatch_straw", "Thatch/straw"),
    ("mud", "Mud"),
    ("metal", "Metal"),
    ("wood", "Wood"),
    ("brick", "Brick"),
    ("tiles", "Tiles"),
    ("slate", "Slate"),
    (OTHER, "Other"),
)

QN39AP = (
    ("daily", "Daily"),
    ("two_day_week", "Two days a week"),
    ("three_day_week", "Three days a week"),
    ("four_day_week", "Four days a week"),
    ("five_day_week", "Five days a week "),
    ("six_day_week", "Six days a week"),
    ("weekly", "Weekly (i.e., once in 7 days)"),
    ("monthly", "Monthly (Once a month)"),
    ("never", "Never"),
)

QN44EAP = (
    ("child", "Child"),
    ("husband", "Husband"),
    ("wife", "Wife"),
    (OTHER, "Other member of the house hold"),
    (NOT_APPLICABLE, "Not applicable"),
)

QN49EAP = (
    ("electricity", "Electricity"),
    ("lpg_natural_gas ", "LPG/Natural gas "),
    ("biogas ", "Biogas "),
    ("kerosene", "Kerosene"),
    ("coal_lignite", "Coal/lignite"),
    ("charcoal", "Charcoal"),
    ("wood", "Wood"),
    ("straw_shrubs_grass ", "Straw/shrubs/grass "),
    ("agricultural_crop", "Agricultural crop"),
    ("animal_dung", "Animal dung"),
    (OTHER, "Other"),
)

QN50EAP = (
    ("kerosene_stove", "Kerosene stove"),
    ("gas_stove", "Gas stove"),
    ("open_fire", "Open fire"),
    ("open_fire_stove", "Open fire or stove with chimney or hood"),
    ("close_stove", "Closed stove with chimney"),
    ("electric_heaters", "Electric heaters"),
    (OTHER, "Other"),
)

INFO_SOURCE = (
    ("patient", "Patient"),
    ("patient_and_outpatient", "Patient, hospital notes and/or outpatient card"),
    ("patient_representive", "Patient Representative (e.family member, friend)"),
    ("hospital_notes", "Hospital notes"),
    ("outpatient_cards", "Outpatient cards"),
    ("collateral_history", "Collateral History from relative/guardian"),
    (NOT_APPLICABLE, "Not applicable"),
    (OTHER, "Other"),
)

VISIT_REASON = (
    (SCHEDULED, "Scheduled visit (study)"),
    (UNSCHEDULED, "Routine / Unscheduled visit (non-study)"),
    (MISSED_VISIT, "Missed visit"),
)

VISIT_UNSCHEDULED_REASON = (
    ("routine_non_study", "Routine appointment (non-study)"),
    ("patient_unwell_outpatient", "Patient unwell"),
    ("drug_refill", "Drug refill only"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

VISIT_REASON_UNSCHEDULED = (
    ("patient_unwell_outpatient", "Patient unwell (outpatient)"),
    ("patient_hospitalised", "Patient hospitalised"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

FAMILY_MEMBERS = (
    ("mother", "Mother"),
    ("father", "Father"),
    ("sister", "Sister"),
    ("brother", "Brother"),
    ("maternal_aunt", "Maternal Aunt"),
    ("maternal_uncle", "Maternal Uncle"),
    ("paternal_aunt", "Paternal Aunt"),
    ("paternal_uncle", "Paternal Uncle"),
    ("maternal_grandmother", "Maternal Grandmother"),
    ("maternal_grandfather", "Maternal Grandfather"),
    ("paternal_grandmother", "Paternal Grandmother"),
    ("paternal_grandfather", "Paternal Grandfather"),
    (OTHER, "Other"),
)

TEST_RESULTS = (
    (POSITIVE, "Positive"),
    (NEGATIVE, "Negative"),
)

TB_TEST_TYPE = (
    ("microscopy", "Microscopy (ZN /Auramine)"),
    ("genexpert", "GeneXpert"),
    ("tb_lam", "TB LAM"),
    (OTHER, "Other"),
)

TB_TEST_RESULT = (
    (POSITIVE, "Positive"),
    (NEGATIVE, "Negative"),
    ("indeterminate", "Indeterminate"),
)

BIOPSY_SIDE = (
    (RIGHT, "Right"),
    (LEFT, "Left"),
)

TYPE_LUNG_CA = (
    ("small_cell", "Small cel"),
    (NON_SMALL_CELL, "Non-small cell"),
)

NON_SMALL_CELL = (
    ("adenocarcinoma", "Adenocarcinoma"),
    ("squamous_cell_carcinomas", "Squamous cell carcinomas"),
    ("large_cell_carcinomas", "Large cell carcinomas"),
    (NOT_APPLICABLE, "Not applicable"),
)

BIOPSY_SITE = (
    ("right_lung", "Right lung (upper, middle or lower)"),
    ("left_lung", "Left lung (upper, middle or lower)"),
    ("pleura", "Pleura"),
)


HIV_DRUG_RESISTANCE = (
    ("NNRTI", "NNRTI"),
    ("NRTI", "NRTI"),
    ("PI", "PI"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

NNRTI = (
    ("DOR", "DOR doravirine"),
    ("EFV", "EFV efavirenz"),
    ("ETR", "ETR etravirine"),
    ("NVP", "NVP nevirapine"),
    ("RPV", "RPV rilpivirine"),
)

NRTI = (
    ("ABC", "ABC abacavir"),
    ("AZT", "AZT zidovudine"),
    ("D4T", "D4T stavudine"),
    ("DDI", "DDI didanosine"),
    ("FTC", "FTC emtricitabine"),
    ("3TC", "3TC lamivudine"),
    ("TDF", "TDF tenofovir"),
)

PI = (
    ("ATV_r", "ATV/r atazanavir/r"),
    ("DRV_r", "DRV/r darunavir/r"),
    ("FPV_r", "FPV/r fosamprenavir/r"),
    ("IDV_r", "IDV/r indinavir/r"),
    ("LPV_r", "LPV/r lopinavir/r"),
    ("NFV", "NFV nelfinavir"),
    ("SQV_r", "SQV/r saquinavir/r"),
    ("TPV_r", "TPV/r tipranavir/r"),
)

HIV_SUBTYPE = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("H", "H"),
    ("K", "K"),
)

HIV_DRUG_RESISTANCE_LEVEL = (
    ("susceptible", "Susceptible"),
    ("low_level_resistance", "Low-Level Resistance"),
    ("high_level_resistance ", "High-Level Resistance "),
)

COOKING_DONE = (
    ("inside_house", "Inside the house"),
    ("outside_house", "Outside the house"),
)

COOKING_AREA = (
    ("window_outside", "Window outside"),
    ("chimney", "Chimney"),
    ("exhaust", "Exhaust"),
    ("partial_open_outside", "Partially open to the outside"),
    ("none", "None"),
)

HIV_SOMATIC_MUTATIONS = (
    ("EGFR", "EGFR"),
    ("KRAS", "KRAS"),
    ("ALK", "ALK"),
    ("HER2", "HER2"),
    ("ROS1", "ROS1"),
    ("MET", "MET"),
    ("BRAF", "BRAF"),
    ("ERBB2", "ERBB2"),
    ("RET", "RET"),
    ("TP53", "TP53"),
    ("CDKN2A", "CDKN2A"),
    ("RAF1", "RAF1"),
    ("MAP2K1", "MAP2K1"),
    ("SMAD4", "SMAD4"),
    ("NRAS", "NRAS"),
    ("AR", "AR"),
    ("FGFR3", "FGFR3"),
    ("PDGFRA", "PDGFRA"),
    ("B2M", "B2M"),
    ("FBXW7", "FBXW7"),
    ("KEAPI", "KEAPI"),
    ("POLE", "POLE"),
    ("PTEN", "PTEN"),
    ("U2AFI", "U2AFI"),
    ("AKT", "AKT"),
    ("ODR2", "ODR2"),
    ("ERBB3", "ERBB3"),
    ("IDH2", "IDH2"),
    ("FGFR4", "FGFR4"),
    ("NMYC", "NMYC"),
    ("ERG", "ERG"),
    ("MTOR", "MTOR"),
    ("FGFR1", "FGFR1"),
    ("APC", "APC"),
    ("CCND1", "CCND1"),
    ("MYC", "MYC"),
    ("CDK4", "CDK4"),
    ("CTNNBI", "CTNNBI"),
    ("RICTOR", "RICTOR"),
    ("CDKN2A", "CDKN2A"),
    ("HRAS", "HRAS"),
    ("KIT", "KIT"),
    ("SMO", "SMO"),
    ("AXL", "AXL"),
    ("FGFR2", "FGFR2"),
)

COOKING_FUEL = (
    (NOT_APPLICABLE, "Not applicable"),
    ("kerosene", "Kerosene"),
    ("charcoal", "Charcoal"),
    ("coal", "Coal"),
    ("gas ", "Gas "),
    ("agricultural_crop", "Agricultural crop"),
    ("wood", "Wood"),
    ("gobar_gas ", "Gobar gas "),
    ("electricity", "Electricity"),
    ("straw_shrubs_grass ", "Straw/shrubs/grass "),
    ("agricultural_crop", "Agricultural crop"),
    ("animal_dung", "Animal dung"),
    (OTHER, "Other"),
)

OTHER_COOKING_FUEL = (
    ("no_other_fuel", "No other fuel except primary fuel used for cooking"),
    ("kerosene", "Kerosene"),
    ("charcoal", "Charcoal"),
    ("coal", "Coal"),
    ("gas ", "Gas "),
    ("agricultural_crop", "Agricultural crop"),
    ("wood", "Wood"),
    ("gobar_gas ", "Gobar gas "),
    ("electricity", "Electricity"),
    ("straw_shrubs_grass ", "Straw/shrubs/grass "),
    ("agricultural_crop", "Agricultural crop"),
    ("animal_dung", "Animal dung"),
    (OTHER, "Other"),
)

FUEL_USED_HEATING = (
    ("no_heating", "No heating during monitoring"),
    ("coal_open_fire", "Coal open fire"),
    ("wood_open_fire", "Wood open fire"),
    ("gas_furnace", "Gas furnace"),
    ("portable_heater", "Portable heater"),
    ("electricity", "Electricity"),
    (OTHER, "Other"),
)

AIR_MONITOR_PROBLEM = (
    ("monitor_fell", "Monitor fell on the surface"),
    ("monitor_noise", "Monitor noise became louder"),
    ("monitor_turned_off", "Monitor turned off before end of period"),
    (OTHER, "Other"),
)

SMOKE_TOBACCO_HOUSE = (
    ("1_times", "Once/day"),
    ("2_4_times", "2-4 times/day"),
    ("5_10_times", "5-10 times/day"),
    ("more_10_times", ">10 times/day"),
    (NOT_APPLICABLE, "Not applicable"),
)

SOLID_FUEL = (
    (NOT_APPLICABLE, "Not applicable; solid fuel was not used for cooking"),
    ("open_fire", "Open fire"),
    ("mud_stove", "Mud stove"),
    ("stove_chimney", "Stove with chimney"),
    ("stove_exhaust_hood", "Stove with exhaust hood"),
    ("stove__builtin_fan", "Stove with built-in fan"),
    ("charcoal_stove", "Charcoal stove"),
)

FOLLOW_UP_TEST = (
    ("chest_xray", "Yes, chest X-ray"),
    ("ct_scan", "Yes, CT scan"),
    ("ultrasound_scan", "Yes, Ultrasound scan"),
    ("blood_cbc", "Yes, Blood CBC"),
    ("chemistry_tests", "Yes, Chemistry tests"),
    (NONE, "None"),
    (OTHER, "Other"),
)

PATIENT_STATUS_VISIT = (
    ("respond_treatment", "Responding to treatment"),
    ("no_changes", "No changes"),
    (NOT_RESPOND_TREATMENT, "Not responding to treatment"),
    ("lost_follow_up", "Lost to follow up"),
    ("died", "Died "),
)

IMM_HIST_CHEM_UP = (
    (POS_TTF1, "Positive- TTF1"),
    (POS_P40, "Positive- P40"),
    (POS_P63, "Positive- P63"),
    (POS_PANCYTOKERATINE, "Positive- PANCYTOKERATINE"),
    (POS_CK20, "Positive- CK20"),
    (POS_CK7, "Positive- CK7"),
    (POS_CK5_6, "Positive- CK5/6"),
    (NEG, "Negative"),
    (NOT_DONE, "Note done"),
)

DEATH_LOCATIONS = (
    ("home", "At home"),
    (HOSPITAL_CLINIC, "Hospital/clinic"),
    ("elsewhere", "Elsewhere"),
)

INFORMANT_RELATIONSHIP = (
    ("husband_wife", "Husband/wife"),
    ("Parent", "Parent"),
    ("child", "Child"),
    (UNKNOWN, "Unknown"),
    (OTHER, "Other"),
)
