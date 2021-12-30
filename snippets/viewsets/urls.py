from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
	UserViewSet,
	SnippetViewSet
	)

# Create router and register viewsets in it.

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('snippets', SnippetViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
	path('', include(router.urls))
]
