from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Used for get and post requests
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer