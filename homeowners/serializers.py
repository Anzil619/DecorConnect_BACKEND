
from professionals.models import FirmInfo,Review
from .models import CustomUser,UserAddress
from professionals.models import Address,Project,ProjectImages
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
from professionals.serializers import ProjectSerializer,ProjectImageSerializer,FirmVerificationSerializer,ReviewSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
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



                


class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        if not user.is_active:
            raise ValidationError('User is not active', code='inactive_user')
        

        print(user.email) # type: ignore
        token['id'] = user.id # type: ignore
        token['email'] = user.email  # type: ignore
        token['role'] = user.role # type: ignore
        token['is_active'] = user.is_active
        token['is_completed'] = user.is_completed  # type: ignore
        

        return token


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProjectSerializers2(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'

    def get_images(self, obj):
        images_queryset = obj.projectimages_set.all()
        images_serializer = ProjectImageSerializer(images_queryset, many=True)
        return images_serializer.data


class FirmsListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    project = ProjectSerializers2(many=True)
    verification = FirmVerificationSerializer()
    reviews = serializers.SerializerMethodField()
    
    
    class Meta:
        model = FirmInfo
        fields = '__all__'

    def get_reviews(self, obj):
        # Fetch reviews for the given firm (obj)
        reviews = Review.objects.filter(firm=obj)
        return ReviewSerializer(reviews, many=True).data


class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = '__all__'


