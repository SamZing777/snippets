from rest_framework import (
	generics, 
	permissions, 
	renderers
	)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippet_app.models import Snippet
from .serializers import SnippetSerializer

from snippet_app.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly]


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = [renderers.StaticHTMLRenderer]

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)
