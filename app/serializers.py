from rest_framework_mongoengine import serializers as mongoserializers
from django.utils import timezone
from mongoengine.queryset.visitor import Q

from app.core.utils import encode_password
from app.models import UserBase, RoleBase


class UserBaseSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = UserBase
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")

        instance.email = validated_data.get('email')
        instance.roles = validated_data.get('roles')
        instance.last_updated_by = request.user.username if str(request.user) != "AnonymousUser" else ''
        instance.last_updated_date = timezone.now()
        instance.save()
        return instance

    def is_user_exist(self, model):
        if not model.get('id') is None:
            query = (Q(username__iexact=model.get('username')) | Q(email__iexact=model.get('email'))) & Q(id__nin=[model.get('id')])
            users = self.Meta.model.objects(query)
        else:
            users = self.Meta.model.objects(
                Q(username__iexact=model.get('username')) | Q(email__iexact=model.get('email'))
            )
        return False if users is None else len(users) >= 1


class RoleBaseSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = RoleBase
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")

        instance.role_name = validated_data.get('role_name')
        instance.description = validated_data.get('description')
        instance.last_updated_by = request.user.username if str(request.user) != "AnonymousUser" else ''
        instance.last_updated_date = timezone.now()
        instance.save()
        return instance

    def is_role_exist(self, model):
        if not model.get('id') is None:
            roles = self.Meta.model.objects(
                Q(role_name__iexact=model.get('role_name')) & Q(id__nin=[model.get('id')])
            )
        else:
            roles = self.Meta.model.objects(role_name__iexact=model.get('role_name'))

        return False if roles is None else len(roles) >= 1
