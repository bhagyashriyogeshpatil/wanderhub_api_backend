from rest_framework import generics, permissions
from wanderhub_api_backend.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of 
    a user following another user.
    Allow users to follow another user when they are logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
  
    def perform_create(self, serializer):
        """
        Save the new follow relationship with 
        the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower and 
    unfollow someone (destroy the relationship) if you are the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer