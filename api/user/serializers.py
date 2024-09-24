from rest_framework import serializers

from user_app.models import User


class UserRegistrationViewSerializer(serializers.ModelSerializer):
    """ Сериализатор вьюшки для регистрации """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')
