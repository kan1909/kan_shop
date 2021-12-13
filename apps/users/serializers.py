from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as SimpleTokenObtainPairSerializer

from utils.celery_tasks import send_verification_email

User = get_user_model()


class TokenObtainPairSerializer(SimpleTokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': _('Активная учетная запись с указанными учетными данными не найдена')
    }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'address',
            'city', 'postcode', 'email', 'phone_number',
            'is_active', 'password',
        )
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.is_active = validated_data.get('is_active', True)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        if validated_data.get('password'):
            print('Password updated')
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    password_repeat = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name',
            'email', 'phone_number',
            'password', 'password_repeat',
        )

    def create(self, validated_data):
        password = validated_data['password']
        password_repeat = validated_data['password_repeat']
        if password == password_repeat:
            user = User.objects.create(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                phone_number=validated_data['phone_number'],
            )
            user.set_password(password)
            user.is_active = False
            user.save()
            send_verification_email.delay(user.email)
            return user
        raise serializers.ValidationError({"password": "Ваши пароли не совпадают."})
