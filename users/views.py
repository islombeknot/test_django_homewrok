from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from django.shortcuts import redirect
from django.http import HttpResponse,  HttpResponseBadRequest



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
