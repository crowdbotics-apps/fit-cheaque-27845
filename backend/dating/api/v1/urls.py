from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    SettingViewSet,
    ProfileViewSet,
    InboxViewSet,
    DislikeViewSet,
    MatchViewSet,
    UserPhotoViewSet,
    LikeViewSet,
)

router = DefaultRouter()
router.register("inbox", InboxViewSet)
router.register("dislike", DislikeViewSet)
router.register("userphoto", UserPhotoViewSet)
router.register("setting", SettingViewSet)
router.register("like", LikeViewSet)
router.register("match", MatchViewSet)
router.register("profile", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
