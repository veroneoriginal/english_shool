from rest_framework import serializers

from user_app.models import User


class UserRegistrationViewSerializer(serializers.Serializer):
    """ Сериализатор вьюшки для регистрации """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

