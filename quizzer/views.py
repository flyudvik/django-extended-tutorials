from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from quizzer import models
from quizzer.forms import QuestionFormSet


class CreateQuizView(CreateView):
    model = models.Quiz
    fields = ['title']
    template_name = 'admin/quizzer/quiz_create.html'

    def get_success_url(self, **kwargs):
        quiz = self.object
        return reverse('quiz-populate-view', args=[quiz.pk])


def quiz_populate(request, quiz_id, *args, **kwargs):
    quiz = models.Quiz.objects.get(pk=quiz_id)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES, instance=quiz)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            formset.save(True)
    else:
        formset = QuestionFormSet(instance=quiz)
    return render(request, 'admin/quizzer/quiz_populate.html', {
        'formset': formset,
        'quiz': quiz
    })
