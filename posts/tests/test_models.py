from django.test import TestCase
from posts.models import *
from ..models import *
from ..views import test_my_function, just_test
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Run once to set up non-modified data for all class metods.')
        pass

    def setUp(self):
        print('setUp: Run once for every test method to setup clean data.')
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(8 < 2)

    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two")
        self.assertEqual(7 * 7, 49)

    def test_signup_form_is_valid(self):
        self.assertFalse(just_test())

    # def test_get_absolute_url(self):
    #     user = User_people.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(user.get_absolute_url(), '/posts/user_info/1')

    def test_one_of_my_function(self):
        print("It is test my project function")
        self.assertEqual(test_my_function(), 2)


    # def test_compare_numbers(self):
    #     post = Posts()
    #     self.assertEqual(post.get_number(), 7)