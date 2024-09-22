from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from savedposts.models import SavedPost


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    saved_post_id = serializers.SerializerMethodField() 

    def validate_image(self, value):
        """
        Validate user uploaded images for
        size, height and width.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the post.
        Returns True if the user is the owner, otherwise False.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieve the ID of the like for the current user on the post.
        Returns the like ID if the user has liked the post,
        otherwise None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_saved_post_id(self, obj):
        """
        Retrieve the ID of the saved post for the current user.
        Returns the saved post ID if the user has saved the post,
        otherwise None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            saved_post = SavedPost.objects.filter(
                owner=user, post=obj
            ).first()
            return saved_post.id if saved_post else None
        return None        

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'place', 
            'region', 'image_filter', 'like_id',
            'saved_post_id'
        ]