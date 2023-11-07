from django.contrib import admin
from .models import Question, Answer, Like  # Import your models

# Register the Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

# Register the Answer model
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'created_at')

# Register the Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'answer')

