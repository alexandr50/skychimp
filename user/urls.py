from django.urls import path

from user.views import RegisterUser, LoginUser, ProfileUser, LogoutUser

app_name = 'user'

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('profile', ProfileUser.as_view(), name='profile'),
    path('logout', LogoutUser.as_view(), name='logout'),
]
