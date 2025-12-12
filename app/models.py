from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    flag = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, default="easy")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Solve(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    submitted_flag = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    solved_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user} - {self.challenge} - {'Correct' if self.is_correct else 'Incorrect'}"  