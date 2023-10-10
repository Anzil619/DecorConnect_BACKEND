from rest_framework.generics import UpdateAPIView
from .models import FirmInfo
from .serializers import EditFirmInfoSerializer

class EditFirmInfo(UpdateAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = EditFirmInfoSerializer

