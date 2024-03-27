from .models import Profile
from django.contrib.auth import get_user
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import re 
from django.contrib.auth.forms import LoginForm
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
    def test_username_already_exists(self):
        user = User.objects.create(username="islombek", first_name="uskir", last_name="baxtiyorjonov", email="isl@gmail.com")
        user.set_password("1234")
        user.save()
        response = self.client.post(
            reverse("username:register"),
            data={
                "username": "islombek",
                "first_name": "Islombek",
                "last_name": "Baxtiyorjonov",
                "email": "islombek@gmail.com",
                "password": "1234"
            }
        )    

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        form = response.context['form']

        self.assertTrue(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

    def test_invalid_email(self):
        response = self.client.post(
            reverse("username:register"),
            data={
                "username": "islombek",
                "first_name": "Islombek",
                "last_name": "Baxtiyorjonov",
                "email": "islombek@gmail.com",
                "password": "1234"
            }
        )    
        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        form = response.context['form']

        self.assertTrue(form.errors)
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

class LoginTestCase(TestCase):
    def test_succel_login(self):
        user = User.objects.create(username="islombek", first_name="uskir", last_name="baxtiyorjonov", email="isl@gmail.com")
        user.set_password("1234")
        user.save()


        self.client.post(
            reverse("users:login"),
            data={
            "username": "islombek",
            "password": "1234"
            }
        )
    


        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)
    

    def testwrongusername(self):
        user = User.objects.create_user(username='kimdur', password='9890')
   
        form_data = {"username": 'kimdur', "password": '9890'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Bunday foydalanuvchi mavjud emas', form.errors['__all__'])


    def test_wrong_password(self):
        
        user = User.objects.create_user(username='kimdur', password='1817')
        
        form_data = {"username": 'kimdur', "password": '1817'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Notogri parol', form.errors['__all__'])

        


class ProfileViewTest(TestCase):
    def setUp(self):
      
        self.user = User.objects.create_user(username='jhon', password='1234')

    def test_profile_view(self):
        self.client.login(username='jhon', password='1234')
        data = {
            'username': 'jhon',
            'first_name': 'John',
            'last_name': 'jhonov',
            'email': 'john@gmail.com',
          
        }
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 302)

     
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.first_name, 'John')
        self.assertEqual(profile.last_name, 'jhonov')
        self.assertEqual(profile.email, 'john@gmail.com')
      



 
