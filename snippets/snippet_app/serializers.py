from rest_framework import serializers

from snippet_app.models import (
	Snippet, 
	LANGUAGE_CHOICES, 
	STYLE_CHOICES
	)


class SnippetSerializer(serializers.ModelSerializer):

	class Meta:
		model = Snippet
		fields = '__all__'
