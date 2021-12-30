from rest_framework import serializers
from django.contrib.auth import get_user_model

from snippet_app.models import Snippet

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	# snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model = User
		fields = ['id', 'username', 'email']
