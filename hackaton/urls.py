"""hackaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path,include
import b_apply.views
import b_bulletin.views
import b_community.views
import b_info.views
import b_login.views
import b_main.views
import b_mypage.views
import b_signup.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup1/', b_signup.views.signup1, name="signup1"),
    path('signup2/', b_signup.views.signup2, name="signup2"),
    path('signup3/', b_signup.views.signup3, name="signup3"),
    path('signup4/', b_signup.views.signup4, name="signup4"),
    path('signup5/', b_signup.views.signup5, name="signup5"),
    path('sendmail/', b_signup.views.sendMail, name="sendMail"),
    path('emailauth/', b_signup.views.emailAuth, name="emailAuth"),
    path('', b_login.views.login, name="login"),
    path('mypage/', b_mypage.views.mypage, name="mypage"),
    path('info/', b_info.views.info, name="info"),
    path('bulletin/', b_bulletin.views.bulletin, name="bulletin"),
    path('create_promo_post/', b_bulletin.views.create_promo_post,
         name="create_promo_post"),
    path('remove_promo_post/<int:promo_id>', b_bulletin.views.remove_promo_post,
         name="remove_promo_post"),
    path('community/', b_community.views.community, name="community"),
    # path('comedit', b_community.update, name="comedit"),
    # path('comread', b_community.comread, name="comread"),
    # path('comregist', b_community.create_post, name="comregist"),
    path('apply/<int:postid>', b_apply.views.apply, name="apply"),
    path('newApply/', b_apply.views.newApply, name="newApply"),
    path('main_yes/', b_main.views.main_yes, name="main_yes"),
    path('regist/', b_info.views.regist, name="regist"),
    path('circle_register/', b_info.views.circle_register, name="circle_register"),

    # mypage url...?

    # path('applySit/', b_mypage.views.applySit, name="applySit"),
    # path('changeProfile/', b_mypage.views.changeProfile, name="changeProfile"),
    # path('changePwd1/', b_mypage.views.changePwd1, name="changePwd1"),
    # path('changePwd2/', b_mypage.views.changePwd2, name="changePwd2"),
    # path('excitingSec/', b_mypage.views.excitingSec, name="excitingSec"),
    # path('extraSave/', b_mypage.views.extraSave, name="extraSave"),
    # path('lastLook/', b_mypage.views.lastLook, name="lastLook"),
    # path('myComment/', b_mypage.views.myCommnet, name="myComment"),
    # path('myGroup/', b_mypage.views.myGroup, name="myGroup"),
    # path('myWrite/', b_mypage.views.myWrite, name="myWrite"),
]
