from django.test import TestCase
from django.contrib.auth import get_user_model




class UserTest(TestCase):

    def test_create_institution_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "test1",
            email= "teste@gmail.com",
            password='Test123'
        )
        self.assertEqual(user.username, 'test1')
        self.assertEqual(user.email, 'teste@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = "admin1",
            email= "admin@gmail.com",
            password='Admintest123'
        )
        self.assertEqual(admin_user.username, 'admin1')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        

