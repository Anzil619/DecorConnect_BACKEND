



from rest_framework_simplejwt.tokens import Token

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from professionals.models import FirmInfo




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if not user.is_active:
            raise ValidationError("user is not active",code='inactive_user')
        
        
        

        print(user.email)   # type: ignore
        token['id'] = user.id # type: ignore
        token['role'] = user.role # type: ignore
        token['name'] = user.name # type: ignore
        token['email'] = user.email # type: ignore 
        token['is_active'] = user.is_active # type: ignore
        token['is_admin'] = user.is_admin # type: ignore

        return token

class FirmUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmInfo
        fields = '__all__'

            