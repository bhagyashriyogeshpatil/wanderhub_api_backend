from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from commentreactions.models import CommentReaction


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')
    commentreaction_id = serializers.SerializerMethodField()
    commentreactions_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField() 

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """Return how long ago
        a comment was created."""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Return how long ago
        a comment was updated."""
        return naturaltime(obj.updated_at)

    def get_commentreaction_id(self, obj):
        """
        Return the ID of the user's reaction to the comment, if any.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            commentreaction = CommentReaction.objects.filter(
                owner=user, comment=obj
            ).first()
            return commentreaction.id if commentreaction else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'created_at',
            'updated_at', 'content', 'commentreaction_id',
            'commentreactions_count' 
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')