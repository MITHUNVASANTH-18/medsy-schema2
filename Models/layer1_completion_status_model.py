from mongoengine import Document,ReferenceField,BooleanField
from Models.user_model import User
from Models.layer_1_model import Layer_1
from Models.component_model import Component


class Layer1_completion_status(Document):
    layer1 = ReferenceField(Layer_1,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    component = ReferenceField(Component,required=True,reverse_delete_rule=2)
    completed=BooleanField(default=False)


    def to_json(self):
        return {
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "component":str(self.component.id) if self.component else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed
        }
    
    def with_key(self):
        return {
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "component":self.component.to_json() if self.component else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed
        }