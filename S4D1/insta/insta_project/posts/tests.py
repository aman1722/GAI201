from django.test import TestCase
from .models import Post

class PostTests(TestCase):

    def test_create_post(self):
        post = Post.objects.create(username="user1", caption="Test caption")
        self.assertEqual(post.username, "user1")
        self.assertEqual(post.caption, "Test caption")

    def test_view_posts(self):
        Post.objects.create(username="user1", caption="Caption 1")
        Post.objects.create(username="user2", caption="Caption 2")

        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caption 1")
        self.assertContains(response, "Caption 2")

    def test_delete_post(self):
        post = Post.objects.create(username="user1", caption="Test caption")
        response = self.client.post(f'/posts/{post.id}/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=post.id).exists())
