
from professionals.models import FirmInfo,Review
from .models import CustomUser,UserAddress,Posts,Like,Comment
from professionals.models import Address,Project,ProjectImages,FirmInfo
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
from professionals.serializers import ProjectSerializer,ProjectImageSerializer,FirmVerificationSerializer,ReviewSerializer,ReviewUserInfo


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


class ListFirmNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmInfo
        fields = ['id','firm_name','status','cover_photo']





class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class CreateLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_profile_photo = serializers.ImageField(source='user.profile_photo', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'



class ListPostSerializer(serializers.ModelSerializer):
    user = ReviewUserInfo()
    like = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = '__all__'

    def get_like(self, obj):
        like = Like.objects.filter(post = obj)
        return CreateLikeSerializer(like, many=True).data
    
    def get_like_count(self, obj):
        return obj.like_set.count()
    
    def get_comments(self,obj):
        comments = Comment.objects.filter(post = obj)
        return CommentSerializer(comments, many=True).data
    
    def get_comments_count(self, obj):
        return obj.comment_set.count()
    



