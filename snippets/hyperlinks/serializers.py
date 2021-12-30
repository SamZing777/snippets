from rest_framework import serializers
from django.contrib.auth import get_user_model

from snippet_app.models import Snippet

User = get_user_model()


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ['url', 'id', 'highlight', 'user', 'title', 'code', 'linenos',
					'language', 'style']


class UserHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'email']
