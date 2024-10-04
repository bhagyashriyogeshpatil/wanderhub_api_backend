from rest_framework import generics, permissions
from wanderhub_api_backend.permissions import IsOwnerOrReadOnly
from .models import CommentReaction
from .serializers import CommentReactionSerializer


# Create your views here.
class CommentReactionList(generics.ListCreateAPIView):
    """
    List all comment reactions, i.e.,
    reactions that users have given to comments.
    Allow users to react to a comment when they are logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentReactionSerializer
    queryset = CommentReaction.objects.all()

    def perform_create(self, serializer):
        """
        Save the new comment reaction with
        the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class CommentReactionDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment reaction and
    allow the owner to delete (remove) it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentReactionSerializer
    queryset = CommentReaction.objects.all()
