from django.contrib import admin
from .models import Challenge, Solve


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'created_at')
    search_fields = ('title', 'description', 'difficulty')
    list_filter = ('difficulty', 'created_at')  
    
@admin.register(Solve)
class SolveAdmin(admin.ModelAdmin):     
    list_display = ('user', 'challenge', 'is_correct', 'solved_at')
    search_fields = ('user__username', 'challenge__title', 'submitted_flag')
    list_filter = ('is_correct', 'solved_at')
   
