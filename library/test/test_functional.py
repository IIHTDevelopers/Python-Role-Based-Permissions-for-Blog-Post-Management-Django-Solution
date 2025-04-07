from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import BlogPost

class BlogPostFunctionalTest(TestCase):

    def setUp(self):
        self.staff_user = User.objects.create_user(username="staff", password="password", is_staff=True)
        self.normal_user = User.objects.create_user(username="user", password="password")

        self.blog = BlogPost.objects.create(title="Sample Blog", content="This is a test blog.", author=self.staff_user)
        self.url = reverse("blog_detail", args=[self.blog.id])

    def test_view_blog_post(self):
        """Test if all users can view a blog post"""
        test_obj = TestUtils()
        try:
            response = self.client.get(self.url)
        except:
            test_obj.yakshaAssert("TestViewBlogPost", False, "functional")
            print("TestViewBlogPost = Failed")
            return
        if response.status_code == 200:
            test_obj.yakshaAssert("TestViewBlogPost", True, "functional")
            print("TestViewBlogPost = Passed")
        else:
            test_obj.yakshaAssert("TestViewBlogPost", False, "functional")
            print("TestViewBlogPost = Failed")

    def test_staff_can_edit_post(self):
        """Test if a staff user can edit a blog post"""
        test_obj = TestUtils()
        try:
            self.client.login(username="staff", password="password")
            response = self.client.post(reverse("blog_edit", args=[self.blog.id]), {"title": "Updated Title", "content": "New Content"})
        except:
            test_obj.yakshaAssert("TestStaffCanEditPost", False, "functional")
            print("TestStaffCanEditPost = Failed")
            return
        if response.status_code == 302:
            test_obj.yakshaAssert("TestStaffCanEditPost", True, "functional")
            print("TestStaffCanEditPost = Passed")
        else:
            test_obj.yakshaAssert("TestStaffCanEditPost", False, "functional")
            print("TestStaffCanEditPost = Failed")
