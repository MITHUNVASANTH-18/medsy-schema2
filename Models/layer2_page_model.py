from mongoengine import Document,ReferenceField,StringField,IntField,ListField
from Models.course_model import Course
from Models.page_content_model import PageContent
from Models.subject_model import Subject
from layer_1_model import Layer_1
from layer_2_model import Layer_2


class Layer2_page(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2,required=True)
    name = StringField(required=True)
    types = StringField(choices=['content','mcq','test_series'],required=True)
    sequence = IntField(required=True)
    hierarcy_level = IntField(default=0)
    child_pages = ListField(ReferenceField(PageContent,reverse_delete_rule=2,required=True))
   
  
    def to_json(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id),
            'name':str(self.name),
            'types':str(self.types),
            'sequence':str(self.sequence),
            'hierarcy_level':str(self.hierarcy_level),
            'child_pages':str(self.name),
            "child_pages":[child_page.to_json() for child_page in self.child_pages] if self.child_pages else None,

        }
