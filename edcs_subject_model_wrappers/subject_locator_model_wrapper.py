from edcs_model_wrapper.wrappers import ModelWrapper


class SubjectLocatorModelWrapper(ModelWrapper):

    model = "edcs_locator.subjectlocator"
    next_url_name = "subject_dashboard_url"
    next_url_attrs = ["subject_identifier"]
