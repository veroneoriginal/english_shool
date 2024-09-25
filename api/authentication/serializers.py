from rest_framework import serializers
from user_app.models import User


class UserRegistrationLoginSerializer(serializers.ModelSerializer):
    """ Сериализатор вьюшки для регистрации и аутентификации """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')
