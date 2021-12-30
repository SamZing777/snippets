from django.contrib.auth import get_user_model
from rest_framework import (
	viewsets, 
	permissions, 
	renderers
	)

from rest_framework.response import Response
from rest_framework.decorators import action

from hyperlinks.serializers import (
	UserHyperLinkedSerializer,
	SnippetSerializer
	)

from snippet_app.models import Snippet
from snippet_app.permissions import IsOwnerOrReadOnly

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):

	# automatically provides "list" and "retrieve" actions

	queryset = User.objects.all()
	serializer_class = UserHyperLinkedSerializer


class SnippetViewSet(viewsets.ModelViewSet):

	"""
		Automatically provides "list", "create", "retrieve", "update",
		and "destroy" actions.

		Additionally, we also provide an extra "highlight" action.
	"""

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly]


	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
