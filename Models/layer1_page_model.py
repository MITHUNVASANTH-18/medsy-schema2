from mongoengine import Document,ReferenceField,StringField,IntField,ListField,DictField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.year_model import Year
from Models.prompt_content_model import Prompt_content


class Layer1_page(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2,required=True)
    name = StringField(required=True)
    types = StringField(choices=['content','mcq','test_series'],required=True)
    sequence = IntField(required=True)
    hierarcy_level = IntField(default=0)
    child_pages = ListField(DictField())
    prompt = ReferenceField(Prompt_content,reverse_delete_rule=2,required=True)    

   
  
    def to_json(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id),
            'name':str(self.name),
            'types':str(self.types),
            'sequence':str(self.sequence),
            'hierarcy_level':str(self.hierarcy_level),
            "child_pages":self.child_pages if self.child_pages else None,
            "prompt": self.prompt
        }
