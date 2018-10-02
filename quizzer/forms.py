from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet, ModelForm

from quizzer import models


class QuestionForm(ModelForm):
    text = forms.CharField(label='Question')

    class Meta:
        model = models.Question
        fields = ['text']


class OptionForm(ModelForm):
    text = forms.CharField(label='Option')

    class Meta:
        model = models.Option
        fields = ['text']


OptionFormSet = inlineformset_factory(models.Question, models.Option, form=OptionForm, min_num=2)


class BaseQuestionFormSet(BaseInlineFormSet):
    # Adds option formsets inside options attribute

    def add_fields(self, form, index):
        super(BaseQuestionFormSet, self).add_fields(form, index)

        form.options = OptionFormSet(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='option_{}_{}'.format(form.prefix, OptionFormSet.get_default_prefix()),
        )

    def is_valid(self):
        result = super(BaseQuestionFormSet, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'options'):
                    result = result and form.options.is_valid()

        return result

    def save(self, commit=True):
        result = super(BaseQuestionFormSet, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'options'):
                if not self._should_delete_form(form):
                    form.options.save(commit=commit)

        return result


QuestionFormSet = inlineformset_factory(
    models.Quiz,
    models.Question,
    formset=BaseQuestionFormSet,
    form=QuestionForm,
    extra=2
)
