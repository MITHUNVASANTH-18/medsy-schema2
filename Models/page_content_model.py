from mongoengine import Document, ReferenceField,StringField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.year_model import Year
from Models.prompt_content_model import Prompt_content


class PageContent(Document):
    course = ReferenceField(Course, reverse_delete_rule=2, required=True)
    year = ReferenceField(Year, reverse_delete_rule=2, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=2, required=True)
    layer1 = ReferenceField(Layer_1, reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2, reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3, reverse_delete_rule=2)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=2)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=2)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=2)
    content = StringField(required=True)
    prompt = ReferenceField(Prompt_content,reverse_delete_rule=2, required=True)
   
    def to_json(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id),
            'year': str(self.year.id),
            "subject": str(self.subject.id),
            "layer1": str(self.layer1.id),
            "layer2": str(self.layer2.id),
            "layer3": str(self.layer3.id),
            "layer1_page": str(self.layer1_page.id),
            "layer2_page": str(self.layer2_page.id),
            "layer3_page": str(self.layer2_page.id),
            "content": self.content,
            "prompt": self.prompt,
        }
