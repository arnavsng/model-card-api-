from app import db

class ModelCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.String(64), unique=True, nullable=False)
    model_summary = db.Column(db.Text)
    model_description = db.Column(db.Text)
    developers = db.Column(db.String(128))
    funded_by = db.Column(db.String(128))
    shared_by = db.Column(db.String(128))
    model_type = db.Column(db.String(64))
    language = db.Column(db.String(64))
    license = db.Column(db.String(64))
    base_model = db.Column(db.String(64))
    repo = db.Column(db.String(256))
    paper = db.Column(db.String(256))
    demo = db.Column(db.String(256))
    direct_use = db.Column(db.Text)
    downstream_use = db.Column(db.Text)
    out_of_scope_use = db.Column(db.Text)
    bias_risks_limitations = db.Column(db.Text)
    training_data_overview = db.Column(db.Text)
    training_data_details = db.Column(db.Text)
    evaluation_results = db.Column(db.Text)
    testing_data = db.Column(db.Text)
    model_examination = db.Column(db.Text)
    hardware_type = db.Column(db.String(64))
    hours_used = db.Column(db.String(64))
    cloud_provider = db.Column(db.String(64))
    cloud_region = db.Column(db.String(64))
    co2_emitted = db.Column(db.String(64))
    model_specs = db.Column(db.Text)
    compute_infrastructure = db.Column(db.Text)
    hardware_requirements = db.Column(db.Text)
    software = db.Column(db.Text)
    citation_bibtex = db.Column(db.Text)
    citation_apa = db.Column(db.Text)
    glossary = db.Column(db.Text)
    more_information = db.Column(db.Text)
    model_card_authors = db.Column(db.Text)
    model_card_contact = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'model_name': self.model_name,
            'model_summary': self.model_summary,
            'model_description': self.model_description,
            'developers': self.developers,
            'funded_by': self.funded_by,
            'shared_by': self.shared_by,
            'model_type': self.model_type,
            'language': self.language,
            'license': self.license,
            'base_model': self.base_model,
            'repo': self.repo,
            'paper': self.paper,
            'demo': self.demo,
            'direct_use': self.direct_use,
            'downstream_use': self.downstream_use,
            'out_of_scope_use': self.out_of_scope_use,
            'bias_risks_limitations': self.bias_risks_limitations,
            'training_data_overview': self.training_data_overview,
            'training_data_details': self.training_data_details,
            'evaluation_results': self.evaluation_results,
            'testing_data': self.testing_data,
            'model_examination': self.model_examination,
            'hardware_type': self.hardware_type,
            'hours_used': self.hours_used,
            'cloud_provider': self.cloud_provider,
            'cloud_region': self.cloud_region,
            'co2_emitted': self.co2_emitted,
            'model_specs': self.model_specs,
            'compute_infrastructure': self.compute_infrastructure,
            'hardware_requirements': self.hardware_requirements,
            'software': self.software,
            'citation_bibtex': self.citation_bibtex,
            'citation_apa': self.citation_apa,
            'glossary': self.glossary,
            'more_information': self.more_information,
            'model_card_authors': self.model_card_authors,
            'model_card_contact': self.model_card_contact
        }