from django.shortcuts import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserRegisterSerializer,myTokenObtainPairSerializer,UserGoogleSerializer
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer



class UserRegistration(APIView):
    def post(self,request):
        email = request.data.get('email')
        print(email)
        password = request.data.get('password')

        serializer = UserRegisterSerializer(data = request.data)
        print(serializer,"anzil")
        if serializer.is_valid(raise_exception=True):
            
            user = serializer.save()
            user.set_password(password)
            user.save()
            
            current_site = get_current_site(request)
            mail_subject = 'please activate your account'
            message = render_to_string('user/account_verification.html',
            {
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
                'site' : current_site

            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()

            return Response({'status' : 'success' , 'msg' : 'a verifiaction link send to your email address', 'data' : serializer.data,})
        else:
            return Response ({ 'status' : 'error', 'msg' : serializer.errors})
        

                            

@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser._default_manager.get(pk=uid)
    except (TypeError,ValueError,OverflowError,CustomUser.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        message = "Congrats, You have been succesfully registered"
        redirect_url =  'http://localhost:5173/login/' + '?message=' + message + '?token' + token
    else:
        message = 'Invalid activation link'
        redirect_url = 'http://localhost:5173/signup/' + '?message=' + message
    
    
    return HttpResponseRedirect(redirect_url)


class GoogleHomeowner(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')


        if not CustomUser.objects.filter(email=email).exists():
            serializer = UserGoogleSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.role = 'homeowner'
                user.is_active = True
                user.is_google = True
                user.set_password(password)
                user.save()

        
        user = authenticate(request, email=email, password=password)
        if user is not None:

            token=create_jwt_pair_tokens(user)

            response_data = {
                'status' : 'success',
                'token' : token,
                'msg' : 'Account has been registered succesfully',
            }

            return Response (data=response_data, status = status.HTTP_201_CREATED)
        else:
            return Response (data={'status' : '400' , 'msg' : 'Login failed'})
        


def create_jwt_pair_tokens(user):
    
    refresh = RefreshToken.for_user(user)

    refresh['email'] = user.email
    refresh['id'] = user.id
    refresh['name'] = user.name
    refresh['role'] = user.role
    refresh['is_active'] = user.is_active

   
    access_token = str(refresh.access_token) # type: ignore
    refresh_token = str(refresh)

    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }