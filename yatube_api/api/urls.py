from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)

from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>.+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/jwt/create/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/', include(router.urls)),
]
