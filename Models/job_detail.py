from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime


class Job_detail(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    created_by=ReferenceField(Admin,required=True,reverse_delete_rule=2)
    created_at = DateTimeField(default=datetime.utcnow)
    target=StringField(choices=['Layer1_page_creation_job','Layer2_page_creation_job','Layer3_page_creation_job'],required=True)
    detail=StringField()
    completed_count=IntField()
    total_count=IntField()
    status=StringField()

    def to_json(self):
        return{
            "course":str(self.course.id) if self.course else None
            ,"created_by":str(self.created_by.id) if self.created_by else None,
            "created_at":str(self.created_at),
            "target":self.target,
            "detail":self.detail,
            "completed_count":self.completed_count,
            "total_count":self.total_count,
            "status":self.status

        }