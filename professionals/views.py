from rest_framework.generics import UpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import FirmInfo,Project,ProjectImages
from .serializers import EditFirmInfoSerializer,ProjectSerializer,ProjectImageSerializer

class EditFirmInfo(UpdateAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = EditFirmInfoSerializer

class EditProject(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EditDeleteProjectImages(RetrieveUpdateDestroyAPIView):
    queryset = ProjectImages.objects.all()
    serializer_class = ProjectImageSerializer
