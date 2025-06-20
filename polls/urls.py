from django.urls import path
from .views import PollListCreateView, PollDetailView, ChoiceCreateView, VoteCreateView

urlpatterns = [
    path('polls/', PollListCreateView.as_view()),
    path('polls/<int:pk>/', PollDetailView.as_view()),
    path('choices/', ChoiceCreateView.as_view()),
    path('votes/', VoteCreateView.as_view()),
]
