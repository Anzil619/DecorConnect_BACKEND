from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from .models import CustomUser
from professionals.models import FirmInfo
from .serializers import UserInfoSerializer,FirmsListSerializer





class SingleUserInfo(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer
    


class FirmsList(ListAPIView):
    serializer_class = FirmsListSerializer
    queryset = FirmInfo.objects.all()

