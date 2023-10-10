from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from .models import CustomUser,UserAddress
from professionals.models import FirmInfo,Project,ProjectImages
from .serializers import UserInfoSerializer,FirmsListSerializer,UserAddressSerializer,ProjectSerializers2
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
    