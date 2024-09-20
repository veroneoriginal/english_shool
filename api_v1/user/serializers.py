from rest_framework import serializers


class UserRegistrationViewSerializer(serializers.Serializer):
    """ Сериализатор вьюшки для регистрации """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
