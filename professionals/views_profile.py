from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.views import APIView
from .models import Project, FirmInfo , FirmVerification,ProjectImages
from .serializers import *






class FirmCreation(ListCreateAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = FirmInfoSerializer



class GetFirmInfo(RetrieveAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = FirmInfoSerializer
    lookup_field = 'user_id'

    def get_object(self):
        user_id = self.kwargs.get(self.lookup_field)
        print(user_id,"anzil")
        return self.queryset.filter(user__id=user_id).first()



class Firm_Completion(UpdateAPIView):
    serializer_class = FirmInfoSerializer
    queryset = FirmInfo.objects.all()
   
    

class FirmVerificationUpdate(UpdateAPIView):
    serializer_class = FirmVerificationSerializer
    queryset = FirmVerification.objects.all()


class CreateProject(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def post(self, request, *args, **kwargs):
    # Extract data from the request
        firm_id = request.data.get('firm_id', None)
        firm_info = FirmInfo.objects.get(id=firm_id)

        # Use the serializer to validate and create the main resource
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            firm_info.project.add(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CreateProjectImages(ListCreateAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()

    def post(self, request):

        project_id = request.data.get('project_id')
        form_data = {}
        form_data['project'] = project_id
        data = []
        flag = True

        print(request.FILES,"anzil")

        for image in request.FILES.getlist('images'):
            form_data['image'] = image
            serializer = ProjectImageSerializer(data=form_data)
            if serializer.is_valid():
                serializer.save()
                data.append(serializer.data)
            else:
                flag = False
            
        if flag:
            return Response(data=data, status=status.HTTP_201_CREATED )
        else:
            return Response(data=[], status=status.HTTP_400_BAD_REQUEST) 

     



        
        
       



    

