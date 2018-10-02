from django.contrib.auth import get_user_model
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    # TODO: add categories, authors and other things


class QuizEntry(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='entries', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='entries', on_delete=models.CASCADE)
    started = models.DateTimeField(auto_created=True)
    finished = models.DateTimeField()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.TextField()


class Answer(models.Model):
    quiz_entry = models.ForeignKey(QuizEntry, related_name='answers', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
