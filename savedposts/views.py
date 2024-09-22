from rest_framework import generics, permissions
from wanderhub_api_backend.permissions import IsOwnerOrReadOnly
from .models import SavedPost
from .serializers import SavedPostSerializer

# Create your views here.


class SavedPostList(generics.ListCreateAPIView):
    """
    List all saved posts, i.e., posts that users have saved.
    Allow users to save a post when they are logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()

    def perform_create(self, serializer):
        """
        Save the new saved post relationship with 
        the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class SavedPostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a saved post and 
    allow the owner to delete (remove) it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()