from django.test import TestCase
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your tests here.

class CommentTestCase(TestCase):
    def setUp(self):
        post_content = 'some content for testing post'
        comment_cotent = 'some content for testing comment'
        Post.objects.create(author='abc', title = 'ddd', text='sssblbblba')
    