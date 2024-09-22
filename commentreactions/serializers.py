from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentReaction

class CommentReactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the CommentReaction model.
    The create method handles the unique constraint on
    'owner' and 'comment'.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentReaction
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        """
        Create a new CommentReaction instance.
        This method checks for duplicate reactions to the same comment
        by the same user. If a duplicate is found, it raises a 
        validation error.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })