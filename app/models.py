from mongoengine import Document, EmbeddedDocument, fields, ListField, ReferenceField
from django.utils import timezone

# Create your models here.


class RoleBase(Document):
    role_name = fields.StringField(required=True, unique=True)
    description = fields.StringField(required=False, null=True)
    creation_date = fields.DateTimeField(default=timezone.now(), null=True)
    created_by = fields.StringField(null=True)
    last_updated_date = fields.DateTimeField(default=timezone.now(), null=True)
    last_updated_by = fields.StringField(null=True)


class UserBase(Document):
    username = fields.StringField(required=True, unique=True)
    email = fields.StringField(required=True)
    password = fields.StringField(required=False, unique=False, null=True)
    is_active = fields.StringField(default='Y')
    creation_date = fields.DateTimeField(default=timezone.now())
    created_by = fields.StringField(null=True)
    last_updated_date = fields.DateTimeField(default=timezone.now())
    last_updated_by = fields.StringField(null=True)

    roles = ListField(ReferenceField(RoleBase))
