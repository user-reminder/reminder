from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics

from user.models import User
from user.permissions import IsOwner
from user.serializers import UserCreateSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
    lookup_field = 'username'
