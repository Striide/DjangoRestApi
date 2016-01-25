from django.test import TestCase
from striide.models import Snippet

class SnippetTestCase(TestCase):
    def setUp(self):
        Snippet.objects.create(title="test1", code="print 'hello'")

    def test_snippets_exist(self):
        """Snippets exist"""
        hello = Snippet.objects.get(title="test1")
        self.assertEqual(hello.code, "print 'hello'")