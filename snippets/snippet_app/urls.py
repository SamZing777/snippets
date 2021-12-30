from django.urls import path

from .views import (
	api_root,
	SnippetList,
	SnippetDetail,
	SnippetHighlight
	)


urlpatterns = [
	path('', api_root),
	path('snippets', SnippetList.as_view(), name='snippets'),
	path('snippets/<int:pk>/', SnippetDetail.as_view(), name='detail'),
	path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view(), name='highlight')
]
