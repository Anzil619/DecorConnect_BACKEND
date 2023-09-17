from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from homeowners.models import CustomUser
from homeowners.serializers import UserInfoSerializer



class ListUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer


class EditDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer

