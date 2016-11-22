from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

class SnippetList(generics.ListCreateAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  # Override the perform_create method so we can add the owner to the
  # Snippet when the Snippet gets saved
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
