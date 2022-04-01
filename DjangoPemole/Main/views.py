from django.shortcuts import render, redirect, get_object_or_404
from Main.models import Photo
from Main.form import RegisterForm
from django.http import request
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User


def Main(request):
    if request.method == 'GET':
        # if request.user.is_active and request.user.is_staff:
        PhotoModelData = Photo.objects.all()
        return render(request, 'Main.html', {'PhotoModelData': PhotoModelData})
    # else:
    #     return redirect('/admin')


def SignUp(request):
    if request.method == 'GET':
        registerForm = RegisterForm()
        return render(request, 'SignUp.html', {'registerForm': registerForm})
    elif request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if not registerForm.is_valid():
            return render(request, 'SignUp.html', {'registerForm': registerForm})
        user = registerForm.save()
        user.set_password(user.password)
        user.save()
        messages.error(request, '註冊成功')
        return redirect(reverse('MainPage:MainPage'))

    # if request.method == 'GET':
    #     if request.user.is_active and request.user.is_staff:
    #         return redirect('/admin')
    #     else:
    #         return render(request, 'SignUp.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password1']
    #     user = User.objects.create_user(username, email, password)
    #     if user:
    #         return redirect('/Main/MainPage', locals())
    #     else:
    #         return redirect('/SignUp', locals())


def Login(request):
    if request.method == 'GET':
        return render(request, 'LoginTp.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # try:
        #     Replace1 = User.objects.get(email=username)
        #     user = authenticate(username=Replace1,password=password)
        # except:
        #     messages.error(request, '資料輸入錯誤')
        #     return redirect('/Main/Login', locals())
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/Main/MainPage', locals())
        else:
            messages.error(request, '資料輸入錯誤')
            return redirect('/Main/Login', locals())



# def Login(request):
#     if request.method == 'GET':
#         return render(request, 'LoginTp.html')
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         CheckEmail = User.objects.filter(email=email)
#         if CheckEmail:
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('/Main/MainPage', locals())
#             else:
#                 messages.error(request, '資料輸入錯誤')
#                 return redirect('/Main/Login', locals())
#         else:
#             messages.error(request, '資料輸入錯誤')
#             return redirect('/Main/Login', locals())


# def Logout(request):
#     auth.logout(request)
#     return redirect('/Main/MainPage')
