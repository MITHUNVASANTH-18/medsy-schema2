from mongoengine import Document, ReferenceField, ListField, DictField, GenericReferenceField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year


class PageContent(Document):
    course = ReferenceField(Course, reverse_delete_rule=2, required=True)
    year = ReferenceField(Year, reverse_delete_rule=2, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=2, required=True)
    layer1 = ReferenceField(Layer_1, reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2, reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3, reverse_delete_rule=2)
    content = ListField(DictField(), required=True)
    page = GenericReferenceField(required=True)
   
    def to_json(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id),
            'year': str(self.year.id),
            "subject": str(self.subject.id),
            "layer1": str(self.layer1.id),
            "layer2": str(self.layer2.id),
            "layer3": str(self.layer3.id),
            "page": str(self.page.id),
            "content": self.content,
        }
