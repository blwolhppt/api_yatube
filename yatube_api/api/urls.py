from django.urls import include, path
from rest_framework import routers, views

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/", include(router.urls)),
]

