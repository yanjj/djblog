from django.test import TestCase
from django.utils import timezone
from blogengine.models import Post

# Create your tests here.

class PostTest(TestCase):
    def test_create_post(self):

        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog test'
        post.pub_date = timezone.now()
        post.save()

        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)
