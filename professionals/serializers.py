
import logging
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Address, FirmInfo, FirmVerification
from homeowners.models import CustomUser




class ProfessionalSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserGoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','name','email','role','is_active','is_google']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FirmVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmVerification
        fields = '__all__'


class FirmInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirmInfo
        fields = '__all__'


class FirmInfoCreateSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    verification = FirmVerificationSerializer()

    class Meta:
        model = FirmInfo
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address', {})
        # firminfo_data = validated_data.pop('FirmInfo')
        verification_data = validated_data.pop('verification')
        print(address_data,'daxo')
        firm_info = FirmInfo.objects.create(**validated_data)
        
        address_serializer = AddressSerializer(data=address_data)
        
        if address_serializer.is_valid():
            address_instance = address_serializer.save()
            firm_info.address = address_instance
           
        verification_serilaizer = FirmVerificationSerializer(data=verification_data)

        if verification_serilaizer.is_valid():
            verification_instance = verification_serilaizer.save()
            firm_info.verification = verification_instance
        

       
        firm_info.save()

            
        

        return firm_info
    

