from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView
from .models import CustomUser,Posts,UserAddress
from professionals.models import FirmInfo,Project,ProjectImages
from .serializers import UserInfoSerializer,FirmsListSerializer,UserAddressSerializer,ProjectSerializers2,ListPostSerializer,ListFirmNameSerializer,CreatePostSerializer
from rest_framework.filters import SearchFilter






class SingleUserInfo(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer
    

class FirmsList(ListAPIView):
    serializer_class = FirmsListSerializer
    queryset = FirmInfo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['firm_name']


class SingleFirmInfo(RetrieveUpdateDestroyAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = FirmsListSerializer
    

class AddUserAddress(CreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class UserAddress(RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    lookup_field = 'user_id'


class GetProject(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers2
    
class ListPost(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = ListPostSerializer


class SuggestionFirm(ListAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = ListFirmNameSerializer


class CreatePost(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreatePostSerializer


class GetUserPosts(ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Posts.objects.filter(user_id=user_id)



