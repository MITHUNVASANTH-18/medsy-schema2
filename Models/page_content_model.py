from mongoengine import Document,ReferenceField,ListField,DictField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.prompt_content_model import Prompt_content

class PageContent(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2,required=True)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2,required=True)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2,required=True)
    prompt = ReferenceField(Prompt_content,reverse_delete_rule=2,required=True)
    content = ListField(DictField(),required=True)
   
    def to_json(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            "subject": self.subject,
            "layer1": self.layer1,
            "layer2": self.layer2,
            "layer3": self.layer3,
            "prompt": self.prompt,
            "content":self.content,
        }
