from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,UpdateAPIView
from homeowners.models import CustomUser
from homeowners.serializers import UserInfoSerializer
from professionals.models import FirmInfo
from .serializers import FirmUpdateSerializer




class ListUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer


class EditDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer


class ApproveFirm(UpdateAPIView):
    queryset = FirmInfo
    serializer_class = FirmUpdateSerializer