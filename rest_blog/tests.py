from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase

from rest_blog.models import Post


class PostTest(SimpleTestCase):
    def setup(self):
        user = User.objects.first()
        Post.objects.create(title='test',content='testing',author=user)


    def test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.content}'
        self.assertEquals(expected_object_name, 'testing')




