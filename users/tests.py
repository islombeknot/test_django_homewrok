from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import re 
# Create your tests here.

class RegisterTestCase(TestCase):

    def test_success_register(self):
        response = self.client.post(
            reverse("user:register"),
            data={
                "username": "islombek",
                "first_name": "Islombek",
                "last_name": "Baxtiyorjonov",
                "email": "islombek@gmail.com",
                "password": "1245"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 1)

        user = User.objects.get(username="islombek")

        self.assertEqual(user.username, "islombek")
        self.assertEqual(user.first_name, "Islombek")
        self.assertEqual(user.last_name, "Baxtiyorjonov")
        self.assertEqual(user.email, "islombek@gmail.com")
        self.assertNotEqual(user.password, "1245")
        self.assertTrue(user.check_password("1245"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("user:register"),
            data={
                "username": "islombek",
                "first_name": "Islombek",
                "last_name": "Baxtiyorjonov",
                "email": "islombek@gmail.com",
                "password": ""
          }
     )
     #    response = response.context['form']


        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertEqual(form.errors['username'], 'This field is required.')
        self.assertEqual(form.errors['username'], 'This field is required.')
    
    
    def test_user_already_exists(self):
       
        response = self.client.post(
            reverse("user:register"),
            data={
                "username": "user",
                "first_name": "islombek",
                "last_name": "baxtiyorjonov",
                "email": "islombek674963@gmail.com",
                "password": "1234"
            }
        )
        form = response.context['form']  
        self.response = response.context['form']
        self.assertEqual(User.objects.count(), 1)  

    def validate_email(email):
     pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
     
     if re.match(pattern, email):
         return True
     else:
         return False
 
