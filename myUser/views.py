from django.shortcuts import render
from django.http import HttpResponse
from myUser.models import CustomUser
from django.contrib import messages

# Create your views here.
from .forms import SignUpForm
def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"sucessfully account created")
        return HttpResponse("account created")
    else:
        return render(request,'signup.html',{'form':form})

    #  if request.method=='GET':
    #     context = {
    #         'form':SignUpForm()
    #     }
    #     return render(request,'signup.html')
    # else:
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("sign success")
    #     return HttpResponse("error occured")
    #     email = request.POST['email']
        # pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']
        # contact = request.POST['contact']
        # if pass1==pass2:
        #     c = CustomUser(email=email,contactNo=contact)
        #     c.set_password(pass1)
        #     c.save()
        #     return HttpResponse("user accont created sucessfully")
        # else:
        #     return HttpResponse("username and password doesnot match")
        #
