from django.urls import path
from .views import ChallengeListView, ChallengeDetailView, SolveChallengeView

urlpatterns = [
    path('', ChallengeListView.as_view(), name='challenge_list'),
    path('<int:pk>/', ChallengeDetailView.as_view(), name='challenge_detail'),
    path('<int:pk>/solve/', SolveChallengeView.as_view(), name='solve_challenge'),
]
