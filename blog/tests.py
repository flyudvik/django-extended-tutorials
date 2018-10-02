from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.utils import create_new_post


class CreatePostTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username='test-user')

    def test_success(self):
        new_post = create_new_post(self.user, 'test title', 'test content')
