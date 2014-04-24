from django.test import TestCase, LiveServerTestCase, Client
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

        self.assertEqual(only_post.title, 'My first post')


class AdminTest(LiveServerTestCase):
    def test_login(self):

        c = Client()
        response = c.get('/admin/')

        self.assertEquals(response.status_code, 200)

        self.assertTrue('Log in' in response.content)

        c.login(username='yanjunjie', password="yanjunjie")

        response = c.get('/admin/')
        self.assertEquals(response.status_code, 200)

class AddPostTest(LiveServerTestCase):
    def test_create_post(self):

        c = Client()
        response = c.get('/admin/blogengine/post/add/')

        self.assertEquals(response.status_code, 200)

        response = self.client.post('/admin/blogengine/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
        },
        follow=True
        )

        self.assertEquals(response.status_code, 200)

        self.assertTrue('added successfully' in response.content)

        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

