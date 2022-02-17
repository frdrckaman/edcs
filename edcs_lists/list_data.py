from edcs_constants.constants import OTHER

list_data = {
    "edcs_lists.covidsymptoms": [
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
    ],

    "edcs_lists.familymembers": [
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
    ],

    "edcs_lists.lungcancersymptoms": [
        ("cough_3_week", "A cough that doesn't go away after 2 or 3 weeks"),
        ("long_standing_cough", "A long-standing cough that gets worse"),
        ("coughing_blood", "Coughing up blood or rust-colored sputum (spit or phlegm)"),
        ("chest_infections", " Chest infections that keep coming back such as bronchitis, pneumonia etc"),
        ("chest_pain_coughing", " Chest pain that is often worsen when breathing or coughing"),
        ("persistent_breathlessness", "Persistent breathlessness"),
        ("tiredness_lack_energy", "Persistent tiredness or lack of energy"),
        ("wheezing", " Wheezing"),
        ("shortness_of_breath", "Shortness of breath"),
        ("unexplained_weight_loss", "Unexplained weight loss"),
        (OTHER, "Other"),
    ],
}

# preload_data = PreloadData(list_data=list_data)
