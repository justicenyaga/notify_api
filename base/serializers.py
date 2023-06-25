from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(UserCreateSerializer):
    is_admin = serializers.SerializerMethodField()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'gender', 'dob', 'id_number',
                  'phone_number', 'county', 'sub_county', 'ward', 'village', 'is_active', 'is_admin')

    def get_is_admin(self, obj):
        return obj.is_staff
