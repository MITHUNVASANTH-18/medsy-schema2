from mongoengine import Document,ReferenceField,DictField,StringField
from Models.component_model import Component
from Models.course_model import Course
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.model_model import Model
from Models.subject_model import Subject
from Models.year_model import Year


class Prompt(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    model = ReferenceField(Model,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,reverse_delete_rule=2)
    subject = ReferenceField(Subject,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    component = ReferenceField(Component,reverse_delete_rule=2)
    prompt_framework = DictField(required=True)
    name=StringField()
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "model":str(self.model.id) if self.model else None,
            "year":str(self.year.id) if self.year else None,
            "subject":str(self.subject.id) if self.subject else None,
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "component":str(self.component.id) if self.component else None,
            "prompt_framework":self.prompt_framework,
            "name":self.name
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "model":self.model.to_json() if self.model else None,
            "year":self.year.to_json() if self.year else None,
            "subject":self.subject.to_json() if self.subject else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "layer2":self.layer2.to_json() if self.layer2 else None,
            "layer3":self.layer3.to_json() if self.layer3 else None,
            "component":self.component.to_json() if self.component else None,
            "prompt_framework":self.prompt_framework,
            "name":self.name
        }
        