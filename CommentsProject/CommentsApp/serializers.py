from rest_framework import serializers

from .models import Comment, Poster, Upvote


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"
