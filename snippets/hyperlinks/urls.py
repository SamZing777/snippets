from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
		SnippetList,
		SnippetDetail,
		SnippetHighlight
	)

from users.views import (
		UserHyperlinkedList,
		UserHyperlinkedDetail
	)

urlpatterns = format_suffix_patterns([
		path('snippets/', SnippetList.as_view(), name='snippet-list'),
		path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
		path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view(), name='snippet-highlight'),
		path('user-list/', UserHyperlinkedList.as_view(), name='user-list'),
		path('user-list/<int:pk>/', UserHyperlinkedDetail.as_view(), name='user-detail')
	])
