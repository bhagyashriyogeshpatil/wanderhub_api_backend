from rest_framework import generics, permissions
from wanderhub_api_backend.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


# Create your views here.
class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if user is
    logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if a user
    owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
