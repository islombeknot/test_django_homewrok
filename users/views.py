from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from .models import Profile
from .forms import RegisterForm, LoginForm,ProfileForm
from django.shortcuts import redirect
from django.http import HttpResponse,  HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer



class RegisterView(View):
     def get(self, request):
         
         form = RegisterForm

         return render(request, 'users/register.html',context={"form":form})
     


     def post(self, request):
          form  = RegisterForm(request.POST)

          if form.is_valid():
               user = form.save(commit=False)
               user.set_password(form.cleaned_data['password'])
               user.save()
               return redirect('landing')
          
          return render(request, 'users/register.html',context={"form":form})
     
     def validate_email(request):
      form = RegisterForm

      if request.method == 'GET':
          email = request.GET.get('email', None)
          if email:
              
               def validate_email_format(email):
                    pass
                 

               if validate_email_format(email):
                    return HttpResponse("Email qabul qilindi .")
               else:
                    return HttpResponse("Noto'g'ri email formati.", status=400)
          else:
               return HttpResponseBadRequest("Email manzili berilmadi.")
      else:
           return HttpResponseBadRequest("So'rov qabul qilinmadi.")
     

      return render(request, 'users/register.html',context={"form":form})

class LoginView(View):

     def get(self, request):
          if request.user.is_authenticated:
              return HttpResponse("page not found")
          form = LoginForm()

          return render(request, 'users/login.html',context={"form":form})
     
     def post(self, request):
          form = LoginForm(request.POST)
          if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(username=username, password=password)
               if user is not None:
                    login(request, user)
                    return redirect("landing")
          return render(request, 'users/login.html',context={"form":form})



# class LoginAPIView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })

     



@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            if profile is None:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
            else:
                form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form})


class LogoutView(LoginRequiredMixin, View):
  def get(self, request):
      logout(request)

      return redirect('landing')
  

def about(request):
    return render(request, 'users/about.html')