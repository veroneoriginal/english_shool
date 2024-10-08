from rest_framework import serializers
from user_app.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для основного класса User"""
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','username', 'phone_number', 'email', 'role']

    def get_role(self, obj):
        return obj.role.first().name if obj.role.exists() else None
