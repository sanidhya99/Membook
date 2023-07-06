from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from .models import CustomUser
from .forms import RegistrationForm
from .manage import UserManager
class SignUpView(CreateView):
    model=CustomUser
    form_class=RegistrationForm
    success_url="/login"
    template_name="register/register.html"
    
# def register(response):
#     if response.method=="POST":
#         # email=response.POST.get["email"]
#         # name=form["name"]
#         # age=form["age"]
#         # gender=form["gender"]
#         # about=form["about"]
#         # password1=form["password1"]
#         # password2=form["password2"]
#         # print(email)
#         form=RegistrationForm(response.POST)

#         print(response.POST)
#         if form.is_valid():
#             print("ke")
#             # if(password1 == password2):
#             form.save()
#             # else:
#             #     raise SystemError("password1!=password2")    
            
#         else:
#             print("lks")
#             messages.error(response, "Invalid form data")    
#     else:
#         form=RegistrationForm()
#     return render(response,'register/register.html',{"form":form,})        


