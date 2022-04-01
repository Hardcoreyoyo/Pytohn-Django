from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def News(request):
    return render(request, 'MainPage/News.html')


@login_required
def Center(request):
    MemberFunc = ["logout",
                  "password/change",
                  "inactive",
                  "email",
                  "password/reset"]

    MemberFuncCh = ["登出",
                    "更改密碼",
                    "帳號狀態",
                    "信箱",
                    "忘記密碼"]

    MemberFuncZip = zip(MemberFunc, MemberFuncCh)

    return render(request, 'MainPage/Center.html', {'MemberFuncZipOut': MemberFuncZip})
