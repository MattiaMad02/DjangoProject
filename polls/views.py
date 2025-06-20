from rest_framework import generics, permissions
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from .permissions import IsOwnerOrReadOnly

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ChoiceCreateView(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

