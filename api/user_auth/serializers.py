from rest_framework import serializers


class UserAuthenticationViewSerializer(serializers.Serializer):
    """ Сериализатор вьюшки для аутентификации"""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
