from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType

from blog.models import Post


def create_new_post(user, title, content):
    new_post = Post.objects.create(user=user, title=title, content=content)
    ct = ContentType.objects.get_for_model(new_post)

    # log_user_action(obj=new_post, actor=user, action='Create new post')
    LogEntry.objects.log_action(
        user_id=user.id,
        content_type_id=ct.pk,
        object_id=new_post.pk,
        object_repr=str(new_post),
        action_flag=CHANGE,
        change_message="New post created")

    return new_post
