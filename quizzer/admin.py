from django.contrib import admin
from django.urls import path, reverse
from django.utils.safestring import mark_safe

from quizzer import views
from quizzer.models import Quiz, Question, QuizEntry


class InlineQuizEntriesAdmin(admin.TabularInline):
    model = QuizEntry
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'populate']
    inlines = [InlineQuizEntriesAdmin]
    # actions_on_top =

    def get_urls(self):
        urls = super().get_urls()
        urlpatterns = [
            path('<int:quiz_id>/populate/', self.admin_site.admin_view(views.quiz_populate), name='quiz-populate-view')
        ]
        return urlpatterns + urls

    def populate(self, obj):
        return mark_safe(
            '<a href="{}">Populate</a>'.format(
                reverse('admin:quiz-populate-view', args=[obj.id])
            )
        )
