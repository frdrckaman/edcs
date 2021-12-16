from edcs_model_wrapper import ModelWrapper


class SubjectRefusalModelWrapper(ModelWrapper):

    model = None  # "myapp.subjectrefusal"
    next_url_attrs = ["screening_identifier"]
    next_url_name = "screening_listboard_url"

    @property
    def pk(self):
        return str(self.object.pk)

    @property
    def screening_identifier(self):
        return self.object.screening_identifier
