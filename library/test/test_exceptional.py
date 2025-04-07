from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from django.contrib.auth.models import User
from library.models import BlogPost



class BlogPostExceptionalTest(TestCase):

    def setUp(self):
        self.staff_user = User.objects.create_user(username="staff", password="password", is_staff=True)
        self.normal_user = User.objects.create_user(username="user", password="password")
        self.blog = BlogPost.objects.create(title="Sample Blog", content="Test content", author=self.staff_user)

    def test_non_staff_cannot_edit(self):
        """Test if non-staff users cannot edit a blog post"""
        test_obj = TestUtils()
        self.client.login(username="user", password="password")
        try:
            response = self.client.post(reverse("blog_edit", args=[self.blog.id]), {"title": "New Title"})
            if response.status_code in [302, 403]:
                test_obj.yakshaAssert("TestNonStaffCannotEdit", True, "exceptional")
                print("TestNonStaffCannotEdit = Passed")
            else:
                test_obj.yakshaAssert("TestNonStaffCannotEdit", False, "exceptional")
                print("TestNonStaffCannotEdit = Failed")
        except:
            test_obj.yakshaAssert("TestNonStaffCannotEdit", False, "exceptional")
            print("TestNonStaffCannotEdit = Failed")