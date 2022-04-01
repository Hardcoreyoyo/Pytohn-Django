"""LearnForAllauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


   ------------------------Urls For Allauth-----------------------------------------

    urlpatterns = [
    url(r"^signup/$", views.signup, name="account_signup"),
    url(r"^login/$", views.login, name="account_login"),
    url(r"^logout/$", views.logout, name="account_logout"),

    url(r"^password/change/$", views.password_change,
        name="account_change_password"),
    url(r"^password/set/$", views.password_set, name="account_set_password"),

    url(r"^inactive/$", views.account_inactive, name="account_inactive"),

    # E-mail
    url(r"^email/$", views.email, name="account_email"),
    url(r"^confirm-email/$", views.email_verification_sent,
        name="account_email_verification_sent"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
        name="account_confirm_email"),

    # password reset
    url(r"^password/reset/$", views.password_reset,
        name="account_reset_password"),
    url(r"^password/reset/done/$", views.password_reset_done,
        name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
        name="account_reset_password_from_key_done"),
]

    path('top_secret/', admin.site.urls),
    path('dont_wanna_tell_u/', include('allauth.urls')),
    path('MainPage/', include('MainPage.urls')),

    dont_wanna_tell_u/ ^ ^signup/$ [name='account_signup']
    dont_wanna_tell_u/ ^ ^login/$ [name='account_login']
    dont_wanna_tell_u/ ^ ^logout/$ [name='account_logout']
    dont_wanna_tell_u/ ^ ^password/change/$ [name='account_change_password']
    dont_wanna_tell_u/ ^ ^password/set/$ [name='account_set_password']
    dont_wanna_tell_u/ ^ ^inactive/$ [name='account_inactive']
    dont_wanna_tell_u/ ^ ^email/$ [name='account_email']
    dont_wanna_tell_u/ ^ ^confirm-email/$ [name='account_email_verification_sent']
    dont_wanna_tell_u/ ^ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
    dont_wanna_tell_u/ ^ ^password/reset/$ [name='account_reset_password']
    dont_wanna_tell_u/ ^ ^password/reset/done/$ [name='account_reset_password_done']
    dont_wanna_tell_u/ ^ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
    dont_wanna_tell_u/ ^ ^password/reset/key/done/$ [name='account_reset_password_from_key_done']
    dont_wanna_tell_u/ ^social/
    dont_wanna_tell_u/ ^google/

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('top_secret/', admin.site.urls),
    path('dont_wanna_tell_u/', include('allauth.urls')),
    path('MainPage/', include('MainPage.urls')),
    path('captcha/', include('captcha.urls')),
]
