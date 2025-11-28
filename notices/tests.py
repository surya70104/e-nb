from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Notice
from django.utils import timezone
from datetime import date

class CategoryModelTest(TestCase):
    def test_str(self):
        c = Category.objects.create(name="General")
        self.assertEqual(str(c), "General")

class NoticeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.cat = Category.objects.create(name="Events")

    def test_create_and_str(self):
        n = Notice.objects.create(
            title="Test Notice",
            content="This is a test.",
            category=self.cat,
            posted_by=self.user,
            expiry_date=date.today()
        )
        self.assertEqual(str(n), "Test Notice")
        self.assertEqual(n.posted_by.username, 'tester')
