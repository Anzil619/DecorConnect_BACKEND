from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Address, FirmVerification, FirmInfo
import base64
from django.core.files.base import ContentFile

from homeowners.models import CustomUser
from .serializers import *
from django.core.files.base import ContentFile



# class profile_completion(APIView):
#     def post(self, request, format=None):
#         try:
#             serializer = FirmInfoSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             validated_data = serializer.validated_data

#             # Create Address instance
#             address_data = validated_data.pop('address')
#             print(address_data,"daxoo")
#             address = Address.objects.create(**address_data)

#             # Create FirmVerification instance
#             verification_data = validated_data.pop('verification')
#             firm_verification = FirmVerification.objects.create(**verification_data)

#             firm_info_data = validated_data.pop('FirmInfo')


#             # Include the user information from the request (modify this as per your API)
#             user_id = request.data.get('user_id')
#             user = CustomUser.objects.get(id=user_id)

#             logo_base64 = validated_data.pop('logoBase64')
#             cover_photo_base64 = validated_data.pop('coverphotoBase64')

#             if logo_base64:
#                 logo_data = base64.b64decode(logo_base64)
#                 FirmInfo.logo.save('logo.png', ContentFile(logo_data), save=True)

#             if cover_photo_base64:
#                 cover_photo_data = base64.b64decode(cover_photo_base64)
#                 FirmInfo.cover_photo.save('cover_photo.png', ContentFile(cover_photo_data), save=True)

#             # Create FirmInfo instance with the user and related data
#             firm_info = FirmInfo.objects.create(
#                 user=user,
#                 address=address,
#                 verification=firm_verification,
#                 **firm_info_data 
#             )

#             return Response("Success", status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(str(e))
#             return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


class profile_completions(ListCreateAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = FirmInfoCreateSerializer

# class CreateFirmInfo(APIView):
    
#     def post(self, request, format=None):
#         # Deserialize the received data
#         firm_info_data = request.data.get('FirmInfo', {})
        
#         address_data = request.data.get('address', {})  
#         verification_data = request.data.get('verification',{})
#         user_id = request.data.get('user_id')
        
#         print(request.data,"annzi")


#         # decoding base64
#         logoBase64=firm_info_data['logoBase64']
#         coverphotoBase64=firm_info_data['coverphotoBase64']

#         logo_data = base64.b64decode(logoBase64)
#         logo = ContentFile(logo_data)

     

#         coverphoto_data = base64.b64decode(coverphotoBase64)
#         cover_photo = ContentFile(coverphoto_data)

#         firm_info_data['logo'] = logo
#         firm_info_data['cover_photo'] = cover_photo

        
#         # Create Address instance
        
#         address_serializer = AddressSerializer(data=address_data)
#         if address_serializer.is_valid():
#             address_instance = address_serializer.save()
#         else:
#             return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # Create Verification instance
#         verification_serializer = FirmVerificationSerializer(data=verification_data)
#         if verification_serializer.is_valid():
#             verification_instance = verification_serializer.save()
#         else:
#             address_instance.delete()  # Rollback Address creation if Verification fails
#             return Response(verification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # Link Address and Verification instances to FirmInfo
#         firm_info_data['address'] = address_instance.id
#         firm_info_data['verification'] = verification_instance.id
#         firm_info_data['user'] = user_id

#         # Create FirmInfo instance
#         firm_info_serializer = FirmInfoSerializer(data=firm_info_data)
#         if firm_info_serializer.is_valid():
#             firm_info_serializer.save()
#             return Response(firm_info_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             address_instance.delete()  # Rollback Address creation if FirmInfo fails
#             verification_instance.delete()  # Rollback Verification creation if FirmInfo fails
#             return Response(firm_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)