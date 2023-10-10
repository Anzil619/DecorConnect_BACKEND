
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Address, FirmInfo, FirmVerification
from homeowners.models import CustomUser
from .models import Address, Project, ProjectImages




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

    def update(self, instance, validated_data):

        instance.owner_name = validated_data.get('owner_name',instance.owner_name)
        instance.owner_pan_card = validated_data.get('owner_pan_card',instance.owner_pan_card)
        instance.firm_liscense = validated_data.get('firm_liscense',instance.firm_liscense)
        instance.gst_certificate = validated_data.get('gst_certificate',instance.gst_certificate)
        instance.insurance = validated_data.get('insurance',instance.insurance)

        instance.save()

        
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class FirmInfoSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required = False)  # Nested serializer for Address
    verification = FirmVerificationSerializer(required = False)  # Nested serializer for FirmVerification
    project = ProjectSerializer(many=True, required = False)

    class Meta:
        model = FirmInfo
        fields = '__all__' 

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', {})        
        owner_name1 = validated_data.pop('data',{})
        print(owner_name1,"nn")
        verification,_ =FirmVerification.objects.update_or_create(owner_name=owner_name1)   
        try:
            verification.gst_certificate = validated_data.get('gst_certificate',verification.gst_certificate)
            print(verification.gst_certificate,"anzil")
            verification.owner_pan_card = validated_data.get('owner_pan_card',verification.owner_pan_card)
            verification.firm_liscense = validated_data.get('firm_liscense',verification.firm_liscense)
            verification.insurance = validated_data.get('insurance',verification.insurance)
            instance.verification = verification
            verification.save()
        except:
            pass
        
        print(instance,"davi")

        # Update fields of the existing instance
        instance.firm_name = validated_data.get('firm_name', instance.firm_name)
        instance.website = validated_data.get('website', instance.website)
        instance.about = validated_data.get('about', instance.about)
        instance.cover_photo = validated_data.get('cover_photo', instance.cover_photo)
        instance.firm_description = validated_data.get('firm_description', instance.firm_description)
        instance.awards = validated_data.get('awards', instance.awards)
        

        # Update or create the related Address  
        if address_data:
            address_instance, _ = Address.objects.update_or_create(**address_data)
            instance.address = address_instance

       
        instance.save()
        return instance



        
    
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'





class EditFirmInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmInfo
        fields = ['id','cover_photo','logo','website','about']




