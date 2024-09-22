from django.db import IntegrityError
from rest_framework import serializers
from .models import SavedPost


class SavedPostSerializer(serializers.ModelSerializer):
    """
    Serializer for the SavedPost model.
    The create method handles the unique constraint on
    'owner' and 'post'.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SavedPost
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Create a new SavedPost instance.
        This method checks for duplicate saved posts by the same user.
        If a duplicate is found, it raises a validation error.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })