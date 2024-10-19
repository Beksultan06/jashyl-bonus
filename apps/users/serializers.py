from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=155, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=155, write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number", "password", "confirm_password"]

    def validate(self, attrs):
        passwords = ['qwerty', '123']

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли отличаются"})
        if any(password in attrs['password'] for password in passwords):
            raise serializers.ValidationError({'confirm_password': "Пароль легкий"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "меньше 8 символов"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Неверные учетные данные")
        else:
            raise serializers.ValidationError("Необходимо указать email и пароль")

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        return validated_data['user']