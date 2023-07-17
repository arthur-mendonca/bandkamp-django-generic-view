from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from .permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
