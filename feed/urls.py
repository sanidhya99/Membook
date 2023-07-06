from django.urls import path
 
from . import views
 
urlpatterns=[
    path("" ,views.home,name="home"),
    path("<int:id>" ,views.view,name="user"),
    path("cmt<int:id>" ,views.cmnt,name="userprofile"),
    path("profile/",views.profile,name="profile"),
    path("users/",views.users,name="users"),
    path("input/",views.input,name="input"),
    path("feed/",views.feed,name="home"),
    path("requests/" ,views.request,name="request"),
    # path("<str:mail>" ,views.viewmail,name="userprofilemail"),

           ]