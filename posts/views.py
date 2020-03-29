from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics#,permissions
from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets #new

# Create your views here.



# class PostList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

'''A viewset is a way to combine the logic for multiple related views into a single class. In
other words, one viewset can replace multiple views. Currently we have four views:
two for blog posts and two for users. We can instead mimic the same functionality
with two viewsets: one for blog posts and one for users.'''

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
