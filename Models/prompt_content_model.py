from mongoengine import Document,ReferenceField,DictField,ListField
from Models.course_model import Course


class Prompt_content(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    system_content = DictField(required=True)
    framework = ListField(DictField())
   
  
    def to_json(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            'system_content':str(self.system_content),
            'framework':str(self.framework),
        }
