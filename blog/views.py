from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from blog.forms import NewPostForm
from blog.utils import create_new_post


class PostCreateView(CreateView):
    form_class = NewPostForm
    success_url = '/success/'
    template_name = 'post_create.html'

    def form_valid(self, form):
        # check for antiplagiat
        # create post
        title, content = form.cleaned_data['title'], form.cleaned_data['content']
        new_post = create_new_post(self.request.user, title, content)
        # return super(PostCreateView, self).form_valid(form)
        return HttpResponseRedirect(self.success_url)
