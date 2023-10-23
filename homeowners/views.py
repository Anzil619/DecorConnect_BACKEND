from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView
from .models import CustomUser,Posts,UserAddress,Like,Comment
from professionals.models import FirmInfo,Project,ProjectImages
from .serializers import UserInfoSerializer,FirmsListSerializer,UserAddressSerializer,ProjectSerializers2,ListPostSerializer,ListFirmNameSerializer,CreatePostSerializer,CreateLikeSerializer,CommentSerializer
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


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
    
class ListPost(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = ListPostSerializer


class SuggestionFirm(ListAPIView):
    queryset = FirmInfo.objects.all()
    serializer_class = ListFirmNameSerializer


class CreatePost(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreatePostSerializer


class GetUserPosts(ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Posts.objects.filter(user_id=user_id)
    

class ListLikes(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = CreateLikeSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Like.objects.filter(post=post_id)
    


class CreateLike(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = CreateLikeSerializer


class Dislike(DestroyAPIView):
    queryset = Like.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        post_id = self.kwargs.get('post_id')  

        print(user_id,"ajmal")
        try:
            like = Like.objects.get(user_id=user_id, post=post_id)
            like.delete()
            return Response({"message": "Like deleted successfully."})
        except Like.DoesNotExist:
            return Response({"message": "Like not found."}, status=404)
        

class CreateComment(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DeleteComment(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DeleteEditPost(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreatePostSerializer
