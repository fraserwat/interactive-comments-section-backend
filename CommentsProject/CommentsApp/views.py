from django.shortcuts import render
from rest_framework import viewsets

from .models import Comment, Poster, Upvote
from .serializers import CommentSerializer, PosterSerializer, UpvoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PosterViewSet(viewsets.ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class UpvoteViewSet(viewsets.ModelViewSet):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer
