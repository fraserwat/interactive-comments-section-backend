from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PosterViewSet, UpvoteViewSet

router = DefaultRouter()
router.register("comments", CommentViewSet)
router.register("posters", PosterViewSet)
router.register("upvotes", UpvoteViewSet)

urlpatterns = [path("", include(router.urls))]
