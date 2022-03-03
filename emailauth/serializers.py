
from rest_framework import serializers
from .models import User, UserProfile
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'age')

class UserRegistrationSerializer(serializers.ModelSerializer):

        password2 = serializers.CharField(label='Confirm Password', write_only=True)
        profile = UserSerializer(required=True)

        class Meta:
            model = User
            fields = ('id', 'username', 'email', 'password', 'password2', 'profile')
            extra_kwargs = {'password':{'write_only':True}}

        def validate(self, data):
            password = data.get('password')
            confirm_password = data.pop('password2')
            if password != confirm_password:
                raise serializers.ValidationError('fasdfadf')
            return data

        def create(self, validated_data):
        # the second param is the default
            profile = validated_data.pop('profile')  

            email = validated_data.get('email')
            username = validated_data.get('username')
            password = validated_data.get('password')
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            UserProfile.objects.create(
                    user=user,
                    first_name=profile['first_name'],
                    last_name=profile['last_name'],
                    phone_number=profile['phone_number'],
                    age=profile['age']
                )
            return user


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.UUIDField(required=False)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            jwt_token = RefreshToken.for_user(user
            )
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token.access_token
        }


class ForgotSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class ChangePassSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=False)

    class Meta:
        model = User
        fields = ('password', 'confirm_password')