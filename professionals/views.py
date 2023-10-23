from rest_framework.generics import UpdateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,RetrieveAPIView
from .models import FirmInfo,Project,ProjectImages,Review
from .serializers import EditFirmInfoSerializer,ProjectSerializer,ProjectImageSerializer,CreateReviewSerializer,UserFirmInfoSerializer

class EditFirmInfo(UpdateAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = EditFirmInfoSerializer

class EditProject(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EditDeleteProjectImages(RetrieveUpdateDestroyAPIView):
    queryset = ProjectImages.objects.all()
    serializer_class = ProjectImageSerializer

class CreateReview(CreateAPIView):
    serializer_class = CreateReviewSerializer
    queryset = Review.objects.all()

class EditReview(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateReviewSerializer
    queryset = Review.objects.all()
    

class FetchUserFirm(RetrieveAPIView):
    serializer_class = UserFirmInfoSerializer
    queryset = FirmInfo.objects.all()
    lookup_field = 'user_id'
