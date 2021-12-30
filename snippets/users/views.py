from rest_framework import generics
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from hyperlinks.serializers import UserHyperLinkedSerializer

User = get_user_model()


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserHyperlinkedList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserHyperLinkedSerializer


class UserHyperlinkedDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserHyperLinkedSerializer
